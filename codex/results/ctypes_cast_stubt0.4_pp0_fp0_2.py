import ctypes
ctypes.cast(0, ctypes.py_object).value

import sys
sys.getrefcount(5)

a = 5
sys.getrefcount(5)

b = 5
sys.getrefcount(5)

del a
sys.getrefcount(5)

del b
sys.getrefcount(5)

import ctypes
ctypes.cast(id(5), ctypes.py_object).value

import ctypes
ctypes.cast(id(5), ctypes.py_object).value = 1

5

a = 5
b = 5
a is b

a = 500
b = 500
a is b

a = 257
b = 257
a is b

a = 257; b = 257
a is b

a = -6
b = -6
a is b

a = -5
b = -5
a is b

a = -4
b = -4
a is b

a = -3
b = -3
a is b

a = -2
b = -2
a is b
