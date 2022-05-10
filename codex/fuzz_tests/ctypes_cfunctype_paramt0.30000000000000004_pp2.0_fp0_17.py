import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def c_callback(x):
    print("c_callback:", x)
    return x + 1

def c_callback2(x):
    print("c_callback2:", x)
    return x + 2

c_callback_func = FUNTYPE(c_callback)
c_callback_func2 = FUNTYPE(c_callback2)

# This is the function we want to call from C.
def my_callback(x):
    print("my_callback:", x)
    return x + 1

# This is the function we want to call from C.
def my_callback2(x):
    print("my_callback2:", x)
    return x + 2

# This is the function we want to call from C.
def my_callback3(x):
    print("my_callback3:", x)
    return x + 3

# This is the function we want to call from C.
def my_callback4(x):
    print("my_callback4:", x)
