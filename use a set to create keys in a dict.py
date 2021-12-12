# assign default values
# retrieve a value from a dict - but assign default value if it is missing (key)

dict1 = {"a": "aaa", "b": "bbb"}
dict2 = {"x": "xxx", "y": "yyy"}
value = dict1.get("z", 0.0)
print(value, dict1)
