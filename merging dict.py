dict1 = {"a": "aaa", "b": "bbb"}
dict2 = {"x": "xxx", "y": "yyy"}
print("dict1 = ", dict1)
print("dict2 = ", dict2)
print(" -  + " * 5, " merge  ")
dict3 = {**dict1, **dict2}
print("dict3 = ", dict3)
print(dict3.values())
print(dict3.keys())
print(" -  + " * 5, " update dict2: create conflict with key 'a'")
dict2["a"] = "ccc"
dict2["d"] = "ddd"
print("dict2 = ", sorted(dict2))

dict3 = {**dict1, **dict2}
print("dict3              = ", dict3)
print("dict3 - but sorted = ", sorted(dict3))
print("keys in dict 1 = ", sorted(dict1.keys()))
print("keys in dict 2 = ", sorted(dict2.keys()))
print("zip both dictonaries = ", list(zip(dict1, dict2)))
