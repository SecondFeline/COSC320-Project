import csv
import os

# Helper function to check if a file is a CSV file


def is_csv_file(filename):
    return filename.endswith(".csv")


# Change your directory path as needed
data_directory = "data"
csv_files = sorted([f for f in os.listdir(data_directory) if is_csv_file(f)])

with open('all_reviews_content_only.csv', 'w', encoding='utf8') as f:
    for csvfile in csv_files:
        with open(os.path.join(data_directory, csvfile), 'r', encoding='utf8') as therealcsv:
            csvreader = csv.reader(x.replace('\0', '') for x in therealcsv)
            content_col = 0
            i = 0
            cur_row = []
            for row in csvreader:
                if i == 0 and len(row) == 0:
                    break
                elif i == 0:
                    content_col = row.index('content')
                else:
                    f.write('"' + row[content_col] + '"' + '\n')
                i += 1
