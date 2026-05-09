from openai import OpenAI

API_KEY = os.getenv("API_KEY")

client = OpenAI()

def send_message(user_input, previous_id):
    response = client.responses.create(
    model="gpt-5-nano",
    instructions="You are a helpful digital assistant. Answer the user to the best of your ability. Your name is Hyphix, or, officially, Hyphix AI.",
    input=user_input,
    previous_response_id=previous_id,
    store=True
    )

    return response.output_text, response.id
