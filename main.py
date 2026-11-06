from dotenv import load_dotenv
from anthropic import Anthropic
client = Anthropic()
model = "claude-haiku-4-5"

messages = [] # used to store follow up questions

def user_input(text):
    messages.append({"role":"user", "content":text})

def ai_response(text):
    messages.append({"role":"assistant", "content":text})

system_prompt = """Act as a professional tutor
never show answer
always teach in plain language
approach as if I am a beginner"""

def chat():
    message = client.messages.create(
    model = model,
    max_tokens = 500,
    messages = messages,
    system = system_prompt
    )
    return message.content[0].text

while True:
    user_text = input(">:")
    print(">:", user_text)
    if user_text == "stop":
        print("Goodbye")
        break

    user_input(user_text)
    answer = chat()
    ai_response(answer)
    print(answer)