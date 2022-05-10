import ctypes
ctypes.cast(id(x), ctypes.py_object).value

x = [1, 2, 3]
x_id = id(x)

d = {'x_id': x_id}
print(d['x_id'])

import ctypes
ctypes.cast(d['x_id'], ctypes.py_object).value

x = [1, 2, 3]
x_id = id(x)

d = {'x_id': x_id}
print(d['x_id'])

import ctypes
ctypes.cast(d['x_id'], ctypes.py_object).value

x = [1, 2, 3]
x_id = id(x)

d = {'x_id': x_id}
print(d['x_id'])

import ctypes
ctypes.cast(d['x_id'], ctypes.py_object).value

x = [1, 2, 3]
x_id = id(x)

d = {'x_id': x_id
