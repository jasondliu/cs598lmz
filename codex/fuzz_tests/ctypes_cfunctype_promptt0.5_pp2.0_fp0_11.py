import ctypes
# Test ctypes.CFUNCTYPE by calling a function that takes a callback
# and passing the callback to it.
import ctypes

def callback(x):
    return x * 2

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def call_func(func):
    return func(2)

call_func(CALLBACKFUNC(callback))

# Test ctypes.addressof() by converting a pointer to an integer and
# back.
import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 42

addr = ctypes.addressof(x)

Xp = ctypes.POINTER(X)

y = Xp.from_address(addr)

y.contents.a == x.a

# Test ctypes.byref() by passing a pointer to a function.
import ctypes

class X(ctypes.Structure):
    _fields_ = [("a
