import os
from groq import Groq

def main():
    english_text = "Artificial intelligence is transforming the world rapidly."
    model = "llama-3.3-70b-versatile"
    prompt = f"Translate the following English sentence into Finnish:\n\n'{english_text}'"
    message = {"role": "user", "content": prompt}

    # Make the API call
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(messages=[message], model=model)
    response = chat_completion.choices[0].message.content
    print(response)


if __name__ == "__main__":
    main()