import os
import random
from openai import OpenAI
from processText import loadDocumentsList

key = os.environ['OPENAI_API_KEY'] # This requires an environment variable- easiest to set it with a CMD (not powershell) terminal

client = OpenAI()

# Load library of text to be worked on

documentsList = loadDocumentsList()

production = True # <-- DEBUGGING

def getInstructions(text):
    return {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are going to be asked to rewrite a part of a story. When doing so, facts about other parts of the story should be factored in, but you should not, for example, write an event that happens in part 1 to happen in part 2, and so on."},
            {
                "role": "user",
                "content": "Rewrite the following short exerpt from a story to be about twice as long overall (by using more sentences, not just longer sentences!) and feature longer conversations. Use your imagination and the system instructions you have been given to flesh out upon the material in the style of a well-written but concise short storylet of about 6 paragraphs. Show, don't tell: when a character feels an emotion, it's better to describe their reaction or have them speak or converse than to state how they feel literally. Rich and evocative word choices are OK, but avoid 'purple prose.'\n" + text + "\n"
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
        
outf = open("script-output.md", "w")

# For each document, put it through the LLM then write it to the output file
for document in documentsList:
    i = ""
    if (document.metadata):     # If the document has metadata, get the contents of the header 4
        i = document.metadata["Header 4"] + "\n"
    i = i + document.page_content # i will now be document.page_Content, prefaced by the header 4 IF there was one
   
    instructions = getInstructions(i)
    
    print("RUNNING LLM on " + instructions["messages"][1]["content"])
    completion = llm(instructions)
    respo = completion.choices[0].message.content
    
    outf.write("### " + document.metadata["Header 4"] + "\n\n")
    outf.write(respo + "\n\n")
    outf.write("---\n\n")

outf.close()
