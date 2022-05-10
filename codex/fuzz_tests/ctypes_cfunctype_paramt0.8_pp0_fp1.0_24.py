import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def c_callback(a, b):
    print(a, b)
    return a + b

c_callback = FUNTYPE(c_callback)

print(c_callback(3, 5))
</code>
In summary:

Python function can be a callback function in C
C function can be a callback function in Python

PS: You can use <code>python-ctypesutils</code> for a cleaner code.

