my_dict_1 = {
    "name": "Sai",
    "city": "Hyderabad"
}

## Getting Values and Keys from Dictionary

# print(my_dict.get('name'))
# print(my_dict.get('city'))

# my_dict.clear()
# print("After Clear: ", my_dict)

my_dict_2 = my_dict_1.copy()
print(my_dict_2)

#get all keys
print(my_dict_2.keys()) #[]

#get all values
print(my_dict_2.values()) #[]


## How to remove a item from Dictionary
#pop
value = my_dict_2.pop('city')
print(value)
print(my_dict_2)

#popitem
my_dict_3 = {'a': 1, 'b': 2, 'c': 3}
popitems = my_dict_3.popitem()
print(popitems)
print(my_dict_3)

## Update a dictionary
my_dict_4 = {'a': 1, 'b': 2, 'c': 3}
my_dict_4.update({'b': 4})
print(my_dict_4)

#setdefault
my_dict_5 = {'a': 1, 'b': 2}
defaultValue = my_dict_5.setdefault('c', 3) #{'c': 3}
print(my_dict_5)