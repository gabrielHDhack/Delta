from groq import Groq
from patterns_and_responses import propt #this is a local script in python

client = Groq(
    api_key="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", #My real API key
)

conversation_history = []  

def get_groq_response(prompt):
    global conversation_history
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"{propt}", # you can use any prompt you want instead of {propt} example: "content": "Your name is JAvis",
            },
            {

                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )
    response = chat_completion.choices[0].message.content
    conversation_history.append((prompt, response))  
    return response

def chatbot():
    global conversation_history
    print("Chatbot: Hello, how can I help you?")
    for prompt, response in conversation_history:
        print(f"You: {prompt}")
        print(f"AI: {response}")

    while True:
        user_input = input("you: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("Chatbot: Bye!!!")
            break
        response = get_groq_response(user_input)
        print(f"AI: {response}")
        conversation_history.append((user_input, response)) 

if __name__ == "__main__":
    chatbot()
