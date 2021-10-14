import csv

file = open('test.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    row.append(row)
print(rows)

file.close()