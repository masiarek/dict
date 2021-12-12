# assign default values
# retrieve a value from a dict - but assign default value if it is missing (key)

dict1 = {"a": "aaa", "b": "bbb"}
dict2 = {"x": "xxx", "y": "yyy"}
value = dict1.get("z", 0.0)
print(value, dict1)

dictionary = {"Mahdi": 555, "Lizbon": 666}

# dict.get() takes a second value as a default
his_apples = dictionary.get("Mahdi", 0)
her_apples = dictionary.get("Jennifer", 0)

print(dictionary.get("Mahdi", 0))
print(dictionary.get("Jennifer", 0))
