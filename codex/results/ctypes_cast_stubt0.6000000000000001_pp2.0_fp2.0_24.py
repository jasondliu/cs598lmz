import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#2.2
x = 10
y = x
x += 5
print(y)

#2.3
x = [1, 2, 3]
y = x
x[1] = 4
print(y)

#2.4
x = [1, 2, 3]
y = list(x)
x[1] = 4
print(y)

#2.5
x = [1, 2, 3]
import copy
y = copy.copy(x)
x[1] = 4
print(y)

#2.6
x = [1, 2, 3]
y = copy.deepcopy(x)
x[1] = 4
print(y)

#2.7
x = [1, 2, 3]
y = x
x = [4, 5, 6]
print(y)

#2.8
x = [1, 2, 3]
y = x
x[:] = [4, 5, 6]
print(y)

#
