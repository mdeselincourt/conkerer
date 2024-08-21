import os
import random
from openai import OpenAI
import processText

key = os.environ['OPENAI_API_KEY'] # This requires an environment variable- easiest to set it with a CMD (not powershell) terminal

client = OpenAI()

# this object is a 'dictionary'
instructions = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are helpful"},
        {
            "role": "user",
            "content": "Confirm you are listening using " + str(random.randrange(1,20)) + " words in the response."
        }
    ]
}


class fauxChatCompletionMessage:
    def __init__(self, content):
        self.content = content

class fauxMessage:
    def __init__(self, message):
        self.message = message

class fauxCompletion:
    def __init__(self, choices):
        self.choices = choices


production = False

def llm(i): 
    if production:
        return client.chat.completions.create(**i) # this ** 'unpacks a dictionary'
    else:
        p = instructions["messages"][1]["content"]
        fccm = fauxChatCompletionMessage("Fake response to '" + p + "'")
        c = fauxCompletion(choices=[fauxMessage(fccm)])
        return c
        
completion = llm(instructions)

print(completion.choices[0].message.content)