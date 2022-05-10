import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("Python callback called with " + str(x))
    return x

callback = FUNTYPE(my_callback)

# Call the C function
lib.call_back(callback)
</code>
Here is the output:
<code>Python callback called with 42
</code>

