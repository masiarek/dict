import numpy as np

ballots_in_dictionary_format = [
    {"Red": 1, "Green": 0, "Yellow": 0, "Blue": 1},
    {"Red": 0, "Green": 1, "Yellow": 0, "Blue": 1},
    {"Red": 1, "Green": 0, "Yellow": 0, "Blue": 1},
]
# test cases used by starpy
columns = ["Allison", "Bill", "Carmen", "Doug"]
election = [
    [5, 4, 1, 4],
    [5, 4, 1, 4],
    [2, 4, 1, 2],
    [4, 3, 2, 1],
    [0, 5, 4, 4],
    [3, 2, 4, 2],
    [3, 1, 5, 3],
    [3, 1, 5, 3],
    [1, 3, 2, 2],
    [4, 3, 5, 5],
]


def convert(source, weighted=False):
    candidates_header = list(source[0].keys())
    scores_temp = []
    for e in source:
        current_row = list(e.values())
        scores_temp.append(current_row)
    return candidates_header, scores_temp


candidates, scores = convert(ballots_in_dictionary_format)
print(candidates)
for e in scores:
    print(e)
