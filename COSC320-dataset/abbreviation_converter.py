import re

# Step 1: Create a dictionary of abbreviations
abbreviations = {
    "WTH": "What The Hell",
    "ASAP": "As Soon As Possible",
    "BTW": "By The Way",
    "DIY": "Do It Yourself",
    "ETA": "Estimated Time of Arrival",
    "FYI": "For Your Information",
    "IDK": "I Don't Know",
    "IMO": "In My Opinion",
    "IMHO": "In My Humble Opinion",
    "OMW": "On My Way",
    "TTYL": "Talk To You Later",
    "WIP": "Work In Progress",
    "TY": "Thank You",
    "LMAO": "Laughing My A** Off",
    "LOL": "Laughing Out Loud",
    "ROFL": "Rolling On the Floor Laughing",
    "ICYMI": "In Case You Missed It",
    "TLDR": "Too Long Didn't Read",
    "TMI": "Too Much Information",
    "LMK": "Let Me Know",
    "NVM": "Nevermind",
    "FTW": "For The Win",
    "NP": "No Problem",
    "JK": "Just Kidding",
    "JW": "Just Wondering",
    "RN": "Right Now",
    "IRL": "In Real Life",
    "DAE": "Does Anyone Else",
    "GG": "Good Game",
    "SMG": "Shaking My Head",
    "NGL": "Not Gonna Lie",
    "IKR": "I Know Right",
    "WTF": "What The F***"
}

# Step 2: Define a function to replace abbreviations in a line


def replace_abbreviations(line, abbrev_dict):
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(key)
                         for key in abbrev_dict.keys()) + r')\b')
    return pattern.sub(lambda x: abbrev_dict[x.group()], line)


input_file = "one_giant_string.txt"
output_file = "converted_giant_string.txt"

# Read the input and process it all line by line
with open(input_file, 'r', encoding='utf-8') as infile:
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Replace abbreviations in the current line
            converted_line = replace_abbreviations(line, abbreviations)
            # Write the converted line to the output file
            outfile.write(converted_line)
print("Conversion completed.")
