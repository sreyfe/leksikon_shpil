import json
from nltk.tokenize import PunktSentenceTokenizer

with open('data.json') as f:
    leksikon = json.load(f)

new_leksikon = []
#remove name from content name -> \n
# remove sources from content "Sources" or "Source"
# split sentences of content
# change case of name
# censor last name in sentences
for entry in leksikon:
    name = entry["name"].title()
    last_name = name.split(" ")[-1]

    content = entry["content"]
    content = content[content.find("\n", content.find("\n")+1) + 1:content.find("\nSource")].strip()

    sent_tokenizer = PunktSentenceTokenizer(content)
    content_split = sent_tokenizer.tokenize(content)
    for i in range(len(content_split)):
        content_split[i] = content_split[i].replace("\n", " ")

    #replace name with █████
    censored_split = []
    for uncensored in content_split:
        censored = uncensored.replace(last_name, "█████")
        censored_split.append(censored)

    new_leksikon.append({"name": name, "content": censored_split})

with open('leksikon.json', 'w') as f:
    json.dump(new_leksikon, f, indent=4)
