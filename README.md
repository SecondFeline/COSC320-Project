# COSC320-Project

## Links

-  Our **Jupyter Notebook** can be found [here](https://github.com/SecondFeline/COSC320-Project/blob/main/COSC320-dataset/milestone3-plots.ipynb)
-  Our final milestone **video** can be found [here](https://youtu.be/fwM99I3LOvQ)

## Introduction

Our project topic involved efficiently replacing abbreviations wtihin a large comma-separated value file of App Store reviews with their full-word equivalents. An abbreviation such as "ASAP" for example, is replaced with "As Soon As Possible" in the output file. We began by taking Dr. Fard's provided dataset and running 2 Python scripts to remove all non-review related information, and then combining all the reviews into one giant string (aptly named, "one-giant-string.txt"). This text file served as our input for 2 different implementations of algorithms for replacing abbreviations.

## Milestones 1 & 3

### Algorithm Description

The proposed algorithm in milestone 1 involved creating a hash table to compare abbreviations to their full-word equivalents. This is a more naïve approach than our next implementation, as we're checking word-by-word comparisons of the .txt file to the abbreviation side of the hash table.

### Implementation Details

In milestone 3, we implemented the algorithm using Python due to its native implementation of hash tables in the form of dictionaries. We first split the text into words, and then iterated through each word, checking if it existed in the abbreviation dictionary. If a match was found, we replaced the abbreviation with its full-word equivalent. This method, while simple, proved to be somewhat slower when processing large datasets such as the one provided by Dr. Fard.

## Milestones 2 & 4

### Algorithm Description

The proposed algorithm in milestone 2 involved creating a trie that stores each known abbreviation and their full-word equivalent at the furthest-most leaf. This data structure allows for more efficient lookups, as the search time is proportional to the length of the abbreviation rather than the size of the dataset.

### Implementation Details

In milestone 4, we implemented the trie-based algorithm in Python. We first created a custom Trie class with methods for inserting and searching abbreviations. Then, we populated the trie with known abbreviations and their corresponding full-word equivalents. When processing the input text, we efficiently searched the trie for abbreviations and replaced them with their full-word equivalents. This method proved to be faster and more scalable when handling larger datasets.

## Conclusion

In conclusion, both the hash table and trie-based approaches were successful in replacing abbreviations with their full-word equivalents in the input dataset. However, the trie-based approach demonstrated better performance and scalability for large datasets. This experiment highlights the importance of choosing the appropriate data structure and algorithm for a given problem in order to achieve optimal efficiency and performance.
