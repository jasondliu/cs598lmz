import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#%%
a = [1,2,3]
b = a
b.append(4)
print(a)

#%%
# mutable and immutable types
# lists are mutable
# tuples are immutable
# strings are immutable
# dicts are mutable
# sets are mutable

#%%
def append_element(some_list, element):
    some_list.append(element)

data = [1,2,3]
append_element(data, 4)
print(data)

#%%
# in-place operators
a = [1,2,3]
a += [4,5]
print(a)

#%%
a = [1,2,3]
b = a + [4,5]
print(a)
print(b)

#%%
a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a + b

#%%
# list comprehension
x = [1,2
