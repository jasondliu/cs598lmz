import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return object()

assert fun() is fun()
try:
    del fun
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

assert fun() is not fun()
try:
    del fun
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

assert fun() is not fun()
try:
    del fun
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# test the __del__ method
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
global called
called = False
class X:
    def __del__(self):
        global called
        called = True
x = X()
@FUNTYPE
def fun(x):
    return x
fun(x)
del x

collect()
if not called:
    raise Exception("__del__ not called")

try:
    del fun
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

#
