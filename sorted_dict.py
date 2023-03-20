my_dict = {'apple': 3, 'banana': 5, 'orange': 2}


sorted_items1 = sorted(my_dict.items(), key=lambda x: x[0])  # Sort by key
print(f'{sorted_items1 = }')
sorted_items1 = [('apple', 3), ('banana', 5), ('orange', 2)]


sorted_items2 = sorted(my_dict.items(), key=lambda x: x[1])  # Sort by value
print(f'{sorted_items2 = }')
sorted_items2 = [('orange', 2), ('apple', 3), ('banana', 5)]


# Sorting a list of lists based on the first element:
data = [[3, 'apple'], [5, 'banana'], [2, 'orange']]
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)
# Output: [[2, 'orange'], [3, 'apple'], [5, 'banana']]

# Finding the minimum value in a list of tuples using the first element:
data = [('apple', 3), ('banana', 5), ('orange', 2)]
min_value = min(data, key=lambda x: x[0])
print(min_value)
# Output: ('apple', 3)

# Sorting a list of dictionaries based on a specific key:
data = [{'name': 'apple', 'price': 3}, {'name': 'banana', 'price': 5}, {'name': 'orange', 'price': 2}]
sorted_data = sorted(data, key=lambda x: x['price'])
print(sorted_data)
# Output: [{'name': 'orange', 'price': 2}, {'name': 'apple', 'price': 3}, {'name': 'banana', 'price': 5}]


my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
sorted_items1 = sorted(my_dict.items(), key=lambda x: x[0])  # Sort by key
print(f'{sorted_items1 = }')
sorted_items1 = [('apple', 3), ('banana', 5), ('orange', 2)]
# Ex2
import pprint
data = [
   {'name': 'apple', 'price': 3},
   {'name': 'banana', 'price': 5},
   {'name': 'orange', 'price': 2},
   {'name': 'kiwi', 'price': 4},
]
sorted_data = sorted(data, key=lambda x: (len(x['name']), -x['price']))
pprint.pprint(sorted_data)
[{'name': 'kiwi', 'price': 4},
 {'name': 'apple', 'price': 3},
 {'name': 'banana', 'price': 5},
 {'name': 'orange', 'price': 2}]

# Ex3 
# Finding the maximum value in a list of dictionaries using the product of 'quantity' and 'price' keys:

data = [
   {'name': 'apple', 'price': 3, 'quantity': 10},
   {'name': 'banana', 'price': 5, 'quantity': 4},
   {'name': 'orange', 'price': 2, 'quantity': 12},
]
max_value = max(data, key=lambda x: x['price'] * x['quantity'])
print(max_value)
{'name': 'apple', 'price': 3, 'quantity': 10}

# Ex4
# Sorting a list of dictionaries based on the 'type' key, then the 'price' key, and finally the 'name' key:
import pprint
data = [
   {'name': 'apple', 'type': 'fruit', 'price': 3},
   {'name': 'banana', 'type': 'fruit', 'price': 5},
   {'name': 'orange', 'type': 'fruit', 'price': 2},
   {'name': 'kiwi', 'type': 'fruit', 'price': 3},
   {'name': 'broccoli', 'type': 'vegetable', 'price': 1},
   {'name': 'carrot', 'type': 'vegetable', 'price': 3},
]
sorted_data = sorted(data, key=lambda x: (x['type'], x['price'], x['name']))
pprint.pp(sorted_data)
[{'name': 'orange', 'type': 'fruit', 'price': 2},
 {'name': 'apple', 'type': 'fruit', 'price': 3},
 {'name': 'kiwi', 'type': 'fruit', 'price': 3},
 {'name': 'banana', 'type': 'fruit', 'price': 5},
 {'name': 'broccoli', 'type': 'vegetable', 'price': 1},
 {'name': 'carrot', 'type': 'vegetable', 'price': 3}]
