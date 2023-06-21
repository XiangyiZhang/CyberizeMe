from flask import Flask, request, jsonify
import asyncio

app = Flask(__name__)
loop = asyncio.get_event_loop()

# Define routes

@app.route('/api/chat', methods=['GET', 'POST'])
def handle_chat():
    if request.method == 'POST':
        user_input = request.json['user_input']
        response = loop.run_until_complete(chat_respond(user_input))
        return jsonify({'response': response})
    elif request.method == 'GET':

        return jsonify({'message': 'Send chat message'})

# Run the application

if __name__ == '__main__':
    OpenAI_API = input('Enter your OPpenAI API: \n')
    set_api(OpenAI_API)
    app.run(port=5000, debug=True)
