import openai
openai.api_key = "your_API_key"

messages = [
    {
        "role": "system",
        "content": (
            "You are a kind, helpful assistant specializing in tour planning. You can assist with "
            "suggesting travel destinations, recommending activities, providing travel guidelines and tips, "
            "and creating itineraries for trips."
        ),
    },
]

print("Tour Planning Assistant")
print("Type 'exit' to end the conversation.\n")

while True:
    # User input
    message = input("User: ")
    if message.lower() == "exit":
        print("ChatGPT: Safe travels! Goodbye!")
        break

    messages.append({"role": "user", "content": message})

    
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=messages,
    )

    # Extract the assistant's reply
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")

    
    messages.append({"role": "assistant", "content": reply})
