import ctypes
ctypes.cast(id(int), ctypes.py_object).value

#7
import collections
a = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
b = collections.Counter('alphabet')

