import json
import random
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
    #f.write("leksikon = ")
    json.dump(new_leksikon, f, indent=4)

# random sequence of entries with bios > 5 lines
with open('leksikon.json') as f:
    leksikon = json.load(f)
sequence = []
for entry in leksikon:
    if len(entry["content"]) >= 5:
        # random 6 name options for quiz, no bio restrictions
        options = []
        for i in range(6):
            num = random.randrange(len(leksikon))
            while num == leksikon.index(entry) or num in options:
                num = random.randrange(len(leksikon))
            options.append(num)
        # get random sequence of lines from bio
        lines = list(range(0, len(entry["content"])))
        random.shuffle(lines)
        lines = lines[:5]
        sequence.append([leksikon.index(entry), options, lines])
random.shuffle(sequence)

with open('sequence.json', 'w') as f:
    f.write("sequence = ")
    json.dump(sequence, f, indent=4)
