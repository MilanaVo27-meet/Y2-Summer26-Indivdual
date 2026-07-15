import os #here we import basically the ai and load everything till the function "run chat"
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY')) #reads the API key to not flash it in the code,it validates the API

def run_chat(): #create a function that will start running the whole thing and by the system we define the Ai's 'personality"
    print('You: (type exit to quit)') 
    system_message = "Your name is John. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity."
    history = [] #here the history of the chat will be saved

    while True: #creating an infinit loop so the code won't stop running till the user texts 'exit'
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        print('History:', history)

        response = client.messages.create( #THE API call. Sends the history of the chat through the API and the Ai answers by the set standarts for the temp and length
            model='claude-haiku-4-5-20251001',
            max_tokens=50,
            temperature=1,
            system=system_message,
            messages=history
        )
        print(response)

#About the usage.input_tokens: it is the cost of our pront andincludes all the text we sent the Ai
#About the usage.output_tokens: it is the size/ cost of the AI/s 


        reply = response.content[0].text #it takes the answer from the AI and shows it on the screen - starts to run the chat
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat() 