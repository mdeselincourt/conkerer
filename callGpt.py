import os
import random
from openai import OpenAI
from processText import loadLibraryList

key = os.environ['OPENAI_API_KEY'] # This requires an environment variable- easiest to set it with a CMD (not powershell) terminal

client = OpenAI()

# Load library of text to be worked on

libraryList = loadLibraryList()

production = False # <-- DEBUGGING

def getInstructions(text):
    return {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are helpful"},
            {
                "role": "user",
                "content": "Summarise this in fewer words: " + text
            }
        ]
    }


def llm(i): 
    if production:
        return client.chat.completions.create(**i) # this ** 'unpacks a dictionary'
    else:
        ### Debugging
        class fauxChatCompletionMessage:
            def __init__(self, content):
                self.content = content

        class fauxMessage:
            def __init__(self, message):
                self.message = message

        class fauxCompletion:
            def __init__(self, choices):
                self.choices = choices

        p = instructions["messages"][1]["content"]
        fccm = fauxChatCompletionMessage("Fake response to '" + p + "'")
        c = fauxCompletion(choices=[fauxMessage(fccm)])
        return c
        ###
        
for document in libraryList:
    instructions = getInstructions(document.page_content)
    completion = llm(instructions)
    print(completion.choices[0].message.content)