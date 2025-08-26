import csv

rows = []

with open('Data.csv', 'r') as file:
    reader = csv.reader(file)
    for item in reader:
        rows.append(item)

itemObject = {}


for item in rows:
   itemObject[item[0]] = [item[2],item[3]]

