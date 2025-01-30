import json
import random

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
    json.dump(sequence, f, indent=4)
