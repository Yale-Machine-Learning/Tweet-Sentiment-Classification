import csv

file = open('dataset/test.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
print(rows)

file.close()