import ctypes
ctypes.cast(p, ctypes.py_object).value = "from ctypes"
print(s)
 
from ctypes import py_object

s = "test string"
p = ctypes.cast(id(s), ctypes.POINTER(ctypes.py_object)).contents
p.value = "from ctypes"
print(s)
 
# ctypes is not the only way to access the internals directly
from sys import intern
intern(s)  # adds s to the table of strings

s = 'hello'
s = s + ' world'  # this creates a new object

s = intern('hello world')


def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t,
