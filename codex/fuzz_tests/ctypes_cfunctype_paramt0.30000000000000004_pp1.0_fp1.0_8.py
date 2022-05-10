import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print "my_callback", x
    return x

callback_func = FUNTYPE(my_callback)

# The following line will cause a segfault
callback_func(1)
</code>
I'm using Python 2.7.3 on Ubuntu 12.04.
I'm not sure what's causing this. I'm also not sure if it's a bug in Python or in my code.
Any ideas?


A:

The callback function needs to be a function with C linkage, not a Python function.  You can use <code>ctypes.CFUNCTYPE</code> to create a function pointer type for a function with C linkage, but you can't use it to create a function pointer to a Python function.

