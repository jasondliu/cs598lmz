import ctypes
ctypes.cast(id(x), ctypes.py_object).value

a = ['Hello', 'World']
b = a
b[0] = 'Goodbye'
a

# copy
a = ['Hello', 'World']
b = a[:]
b[0] = 'Goodbye'
a

# recursive
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
b.append(a)
a

# List Comprehensions
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

squares = map(lambda x: x ** 2, a)
print(squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert alt == [4, 16, 36, 64, 100]

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict =
