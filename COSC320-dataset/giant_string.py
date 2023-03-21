import csv, os, re

with open('one_giant_string.txt', 'w', encoding='utf8') as f:
    for csvfile in os.listdir('data'):
        with open('data/' + csvfile, 'r', encoding='utf8') as therealcsv:
            csvreader = csv.reader(x.replace('\0', '').replace('\r\n', '') for x in therealcsv)
            content_col = 0
            i = 0
            cur_row = []
            for row in csvreader:
                if i == 0 and len(row) == 0:
                    break
                elif i == 0:
                    content_col = row.index('content')
                else:
                    f.write(re.sub(r'[\n\r\u2028\u2029]+', ' ', row[content_col] + ' '))
                i += 1
