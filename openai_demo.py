from openai import OpenAI

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

rle = "user"
mdl = "gpt-3.5-turbo"
cnt = "How to bulk rename files using regex in bash using grep, sed"

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model=mdl,
    messages=[
        {
            "role": rle, 
            "content": cnt, 
        },
    ],
)
print(completion.choices[0].message.content)

