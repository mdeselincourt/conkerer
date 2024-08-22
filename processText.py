from langchain_text_splitters import MarkdownHeaderTextSplitter

def loadDocumentsList():

    with open('step2.md', 'r') as file:
        file_contents = file.read()

        headers_to_split_on = [
        ("####", "Header 4"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

    documents_list = markdown_splitter.split_text(file_contents) # This creates Document objects, use .page_content

    #print(documents_list[1].metadata["Header 4"])

    return documents_list
