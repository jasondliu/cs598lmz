import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

def my_callback(num):
    print("got", num)

# convert the Python callback into a C callback
c_callback = FUNTYPE(my_callback)

# call a C function that takes a callback as an argument
lib.call_a_c_function(c_callback)
</code>

