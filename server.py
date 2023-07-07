from flask import Flask, request, jsonify
import time
import threading
import asyncio
from Session import Session

app = Flask(__name__)
loop = asyncio.get_event_loop()

OPENAI_API_KEY=''
AGENT_NAME='Sam'

# Global session manager
session_manager = {}

# Define routes
@app.route('/api/chat', methods=['GET', 'POST'])
async def handle_chat():
    if request.method == 'POST':
        message = request.json['message']
        sender = request.json['sender']

        if sender not in session_manager:
            session_manager[sender] = Session(OPENAI_API_KEY=OPENAI_API_KEY,
                                            agent_name=AGENT_NAME,
                                            sender=sender)
        session = session_manager[sender]
        response = await session.reply(message)
        session.update_interaction_time()
        
        return jsonify({'response': response})
    elif request.method == 'GET':

        return jsonify({'message': 'Send chat message'})

# Run the application

# Session expiration thread
def session_expiration_check():
    while True:
        for sender in list(session_manager.keys()):
            if session_manager[sender].is_expired():
                session_manager[sender].end_session()
                del session_manager[sender]
        time.sleep(60)  # checks every minute

if __name__ == '__main__':
    threading.Thread(target=session_expiration_check, daemon=True).start()
    app.run(port=5000, debug=True)
