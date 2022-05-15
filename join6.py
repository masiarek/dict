import csv
ra =  csv.DictReader(open('a.csv'))
all_keys = set()
for e in ra:
    print(e)