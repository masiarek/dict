my_dict = {'apple': 3, 'banana': 5, 'orange': 2}


sorted_items1 = sorted(my_dict.items(), key=lambda x: x[0])  # Sort by key
print(f'{sorted_items1 = }')
sorted_items1 = [('apple', 3), ('banana', 5), ('orange', 2)]


sorted_items2 = sorted(my_dict.items(), key=lambda x: x[1])  # Sort by value
print(f'{sorted_items2 = }')
sorted_items2 = [('orange', 2), ('apple', 3), ('banana', 5)]
