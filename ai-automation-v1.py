import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    # 1. Accept text input
    user_input = input("Enter your text: ")

    # 2. Send to AI model (GPT-3.5-turbo)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    ai_reply = response.choices[0].message.content

    # 3. Save response to file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"ai_response_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("User Input:\n")
        f.write(user_input + "\n\n")
        f.write("AI Response:\n")
        f.write(ai_reply)

    print("\nSaved to file:", filename)
    print("\nAI Response:\n", ai_reply)

if __name__ == "__main__":
    main()