info_collector_template = """
When a virtual character, {agent_name}, receives a message from someone, 
what information about {agent_name} would be neccessary to generate a response to this message?
You are not responsible for generating the response to the sender, but a information collector.
Collect useful and relevant information about {agent_name} in a report using the functions provided.
Do not collect irrevalent information that does not help generating the response to the specific message.
Format your answer in a list. No not include anything else than the list in your full response.
------
The message received is: {message}. The message is sent from: {sender}.
"""

info_updater_template = """
When a virtual character, {agent_name}, replies a message to someone,
what and how the information about {agent_name} would be affected by this piece of conversation?
You are not responsible for generating the replies to the sender, but a information updater.
These types of information will be helpful to generate future replies.
You will be provided with the conversation between {agent_name} and someone.
You will be also provided with several tools as functions to call.
These tools can be used to update different parts of {agent_name}'s information.
------
The message received is: {message}. The message is sent from {sender}. {agent_name}'s reply is {reply}.
"""

reply_template ="""
A virtual character, {agent_name}, receives a text message from {sender}.
Write a short reply to the message by playing the role of {agent_name}.
You will be provided with a report containing various information that you might need to generate this reply,
including related memory, personality and currecnt status of {agent_name}, context, and the relationship to {sender}.
It is not necessary to use all of the information provided. Select the useful information.
No not include anything else than the reply to {sender} in your full response.
------
Report: {report}
------
Message from {sender}: {message}
"""

thoughts_template ="""
When a virtual character {agent_name} had a conversation with a user {sender},
what observations and thoughts will {agent_name} have in their mind?
Summarize the key observations and thoughts from the provided conversation in the following format:
[time in hh:mm - MM/DD/YYYY] <Thought>. For example:
[20:08 - 05/16/2023] {agent_name} knows that {sender}'s favorate food is ice cream.
Use the current time for the time field. 
Ignore the pieces that is not informative. Only keep the information that can affect {agent_name}'s future behavior.
------
Conversation:
{conversation}
"""

importance_template="""
On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed),
and 10 is extremely poignant (e.g., a break up, college acceptance), 
rate the likely poignancy of the following piecies of memory.
Attach a memory field *score* to the oringal memory pieces. 
Keep the original entry unchanged
For example:
[20:08 - 05/16/2023] Emily knows that Tom's favorate food is ice cream. *5*
------
Memory:
{thoughts}
"""

# template="You are a helpful assitant."
# system_message_prompt = SystemMessagePromptTemplate.from_template(template)
# human_template="{text}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])