import re

abbreviation_table = {
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


def replace_abbreviations(match):
    abbreviation = match.group(0).upper()
    return abbreviation_table.get(abbreviation, abbreviation)


# Regular expression pattern for matching abbreviations
abbreviations = list(abbreviation_table.keys())
abbreviation_pattern = re.compile(
    r'\b(?:' + '|'.join(re.escape(abbr) for abbr in abbreviations) + r')\b', re.IGNORECASE)

input_file = "one_giant_string.txt"
output_file = "converted_text.txt"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        converted_line = abbreviation_pattern.sub(replace_abbreviations, line)
        outfile.write(converted_line)

print("Abbreviations replaced and output saved in", output_file)
