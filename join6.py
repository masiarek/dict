import csv
from collections import defaultdict

ra = csv.DictReader(open("a.csv"))
rb = csv.DictReader(open("b.csv"))
rc = csv.DictReader(open("c.csv"))
all_keys = set()
print("a", list(ra))
dd = defaultdict(list)
# for e in ra:
#     all_keys.add(e['ak'])
#     dd.append[e['ak']]
# for e in rb:
#     all_keys.add(e['bk'])
#
# for e in rc:
#     all_keys.add(e['ck'])

print(sorted(all_keys))
dd.update(ra)
print((dd))

print("testttt3")
