import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

#%%
x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)

#%%
# The * operator can be used in any context where it makes sense to pass elements as separate arguments
print(*zip(x, y))

#%%
# The zip() function in Python 3 returns an iterator. If you need the reversed list, you can convert it to a list with list()
print(list(zip(x, y)))

#%%
# The zip() function stops when the shortest input iterable is exhausted.
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
list(zip(x, y))

#%%
# zip() can accept a variable number of iterables.
x = [1, 2, 3]
y = [4, 5, 6
