import types
types.ModuleType

# lists
my_list = [1, 2, 2, 'hello', 3.2]
# lists are mutable
my_list[1] = 3

# slicing
my_list[1:3]
my_list[1:-1]
my_list[-1]

# add
my_list + [4, 5]

# del
del(my_list[2])

# append
my_list.append('new element')


# tuple
my_tuple = (1, 2, 'hello', 3.2)
# tuples are immutable
my_tuple[1] = 2

# unpacking
a, b, c = (1, 2, 3)

# zip
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
list(zip(list_1, list_2))


# sets
my_set = {1, 2, 3, 3}

# formatting
str_1 = 'Value 1: {a}, value 2: {b}, value 3: {
