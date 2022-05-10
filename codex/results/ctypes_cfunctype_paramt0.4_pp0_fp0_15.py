import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print(a, b)
    return a + b

callback = FUNTYPE(my_callback)

print(callback(1, 2))
</code>
This is what I have so far:
<code>import ctypes

def my_callback(a, b):
    print(a, b)
    return a + b

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(my_callback)

print(callback(1, 2))
</code>
But I get the following error:
<code>TypeError: wrong type
</code>
I'm not sure what I'm doing wrong.


A:

The error is because <code>my_callback</code> is not a C function that can be called.  It's a Python function.  You can't pass a Python function to a C function expecting a C function.  You can't even pass
