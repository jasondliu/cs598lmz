import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print('callback called with', i)
    return 0

# convert the Python callback into C callback
cb = FUNTYPE(my_callback)

# call a library function using the C callback
lib.do_something(2, cb)
</code>
The above works fine, but I am wondering if there is any way to pass a Python function directly to the C library function, without the need to create the C callback?

