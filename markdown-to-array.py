from processText import markdownFileToJavascriptArray

paragraphs = markdownFileToJavascriptArray('step3b.md')

outf = open("content-array-file.js", "w", encoding='utf-16')

outf.write("const chapters = [];\n\n")

for i, value in enumerate(paragraphs):
    outf.write(f"chapters[{i}] = `{value}`;\n\n")

print('\nDone\n')