import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return range(10)
fun()

# Simple callback function
from ctypes import c_int, WINFUNCTYPE, windll
from time import sleep

# Prototype and return type of the callback functions
prototype = WINFUNCTYPE(c_int, c_int, c_int)

# Function to register as callback
def py_add(a, b):
    print("Python got", a, b)
    return a + b

# Convert the Python function into a callable C function
c_add = prototype(("add", windll.kernel32), ((1, "a"), (1, "b")))

# Register the C function as a callback
windll.kernel32.SetTimer(None, 0, 500, c_add) 

while True:
    sleep(1.0)
