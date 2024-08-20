import os
from openai import OpenAI

key = os.environ['OPENAI_API_KEY'] # This requires an environment variable- easiest to set it with a CMD (not powershell) terminal

client = OpenAI()

instruction = {
    
}

# this object is a 'dictionary'
instructions = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are helpful"},
        {
            "role": "user",
            "content": "Confirm that are listening using the word dictionary."
        }
    ]
}



completion = client.chat.completions.create(**instructions) # this 'unpacks a dictionary'

print(completion.choices[0].message)