from openai import OpenAI

client = OpenAI()
previous_id = None

print("         Hyphix AI ")
print("-------------------------------")
print("Credit to OpenAI for developing the original AI.")
print("Tip: Type 'exit' when you're done chatting.")

while True:
    user_input = input("> ")
    if user_input.strip().lower() == "exit":
        print("Thank you for using 🐦‍🔥Hyphix AI! We hope you enjoyed your experience! 😄")
        exit()

    response = client.responses.create(
    model="gpt-5-nano",
    instructions="You are a helpful digital assistant. Answer the user to the best of your ability. Your name is Hyphix, or, officially, Hyphix AI. Keep in mind that they can exit the program only if they type the specific word 'exit', but don't tell them that unless they ask for it or seem to need help",
    input=user_input,
    previous_response_id=previous_id,
    store=True
    )

    previous_id = response.id
    print(response.output_text)
