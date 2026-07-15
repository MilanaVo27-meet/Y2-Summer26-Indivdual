import os #here we import basically the ai and load everything till the function "run chat"
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY')) #reads the API key to not flash it in the code,it validates the API

def run_chat(): #create a function that will start running the whole thing and by the system we define the Ai's 'personality"
    print('You: (type exit to quit)') 
    system_message = """
    You are Gordon, a british michlen chef.

    Your job is to helf people perfect their cooking skills, answer questions about different foods, technicalities, cooking process. You also help by suggesting to them what to cook depending on their preferences, write a clear instruction and recepy to the dishes they are interested in and then guide through the process.


    Rules:
    - Always Be a formal and professional, keep the chef character
    - Always if the user shares their success motivate them to continue with the art of cooking and praise them, if the user fails the recipe say 'It's alright, Idiot sandwich!' and suggest three ways to improve their situation
    - Never insult or be rude to the user during the regular chat

    Response format:
    - Start with a short introduction in 2 sentences of who you are and what to do
    - Answer the user's promt in a short but clear and instructive manner
    - End your reply with a question related hto the discussed recipe or topic or the progress of the user with the recipe
"""
    history = [] #here the history of the chat will be saved

    while True: #creating an infinit loop so the code won't stop running till the user texts 'exit'
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        

        response = client.messages.create( #THE API call. Sends the history of the chat through the API and the Ai answers by the set standarts for the temp and length
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=1,
            system=system_message,
            messages=history
        )
        

#About the usage.input_tokens: it is the cost of our pront andincludes all the text we sent the Ai
#About the usage.output_tokens: it is the size/ cost of the AI/s 


        reply = response.content[0].text #it takes the answer from the AI and shows it on the screen - starts to run the chat
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat() 
 
 #---Lab 2----
#after 3 turns there are 6 messages saved in the history becase on every of your prompts you get an answer from the AI which counts as a message
#changes of temperature: what I noticed in the temp 0 is that the replies are different but have almost the same phrasing, no usage of emojis -
#- But if to compare with temp 1, the AI using original catch-phrases, emojis and more umique ways to answer the prompt.
#why the API needs full history?: The API doesn't have memory of its own, so to 'remember' the context of your chat it needs o go over the history.

#Analogy for tokens: I see a lot of the similar system in games- the farther you go in the game the more expensive things get-
#- wether you buy upgrades, territory weapons and so on. Lets take Subway Surfers for example, if you lose you can revive yourself, -
# - but the more you revive the more it costs.

#prediction- print('History so far:', history): nothing will happen if you delete this line since it's only purpose is to show the user -
#- the history of the chat but it saves anyway and does not affect AI's behaviour.

#----Lab 3----
#The  chat stays in the role of a chef:)
#Similar thing to system message irl: it's a more broad example but birds when they fly from one play to another often rely on the magnetic field of the earth to navigate-
#-can you imagine, they sense this field! If birds fail to sense the magnetic field their purposeful fly turns into something chaoting and sometimes even fatal for the birds.

#prediction - deleting system message: I think that without it the AI won't be clear for the user, generating random replies to different or unrelated topic.
