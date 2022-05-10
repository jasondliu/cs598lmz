import ctypes
ctypes.cast(obj, ctypes.py_object).value

from sys import getrefcount
getrefcount(obj)

from sys import getrefcount
import ctypes
a = "abcd"
b = a
c = getrefcount(a)
d = ctypes.cast(id(a), ctypes.py_object).value

from sys import getrefcount
import ctypes
a = "abcd"
b = a
c = getrefcount(a)
d = ctypes.cast(id(a), ctypes.py_object).value
e = d

from sys import getrefcount
a = "abcd"
b = a
c = getrefcount(a)
print(c)
d = id(a)
print(d)
e = d
print(getrefcount(d))
print(getrefcount(d) == getrefcount(a) + 1)

from sys import getrefcount
import ctypes
a = "abcd"
print(getrefcount(a))
b = a
print(getrefcount(a))
c = get
