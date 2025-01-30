import json
from nltk.tokenize import PunktSentenceTokenizer

with open('data.json') as f:
    leksikon = json.load(f)

new_leksikon = []
#remove name from content name -> \n
# remove sources from content "Sources" or "Source"
# split sentences of content
# change case of name
for entry in leksikon:
    name = entry["name"].title()
    content = entry["content"]
    content = content[content.find("\n", content.find("\n")+1) + 1:content.find("\nSource")].strip()
    sent_tokenizer = PunktSentenceTokenizer(content)
    content_split = sent_tokenizer.tokenize(content)
    for i in range(len(content_split)):
        content_split[i] = content_split[i].replace("\n", " ")
    new_leksikon.append({"name": name, "content": content_split})

with open('leksikon.json', 'w') as f:
    json.dump(new_leksikon, f, indent=4)
