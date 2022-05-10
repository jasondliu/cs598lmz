import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello, world!")
    return 123
print("fun is:", fun)
fun()

print("="*30)
print("Python library API:")
import libtest
print("libtest.add(3.25, 4.75) returns", libtest.add(3.25, 4.75))
print("class from libtest")
x = libtest.values()
print("has attrs:", dir(x))
print("libtest.values.add(4.25, 5.75) returns", x.add(4.25, 5.75))
i = libtest.some_function()
print("libtest.some_function() returns", type(i), i)
print("libtest.some_function() returns", libtest.some_function())
j = libtest.other_function(ctypes.c_int(123))
print("libtest.other_function(123) returns", type(j), j)

print("="*30)
print("Python library API (1):")
class X:
    def __init__(self):
        self
