import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with", x)
    return x + 1

my_callback_c = FUNTYPE(my_callback)

# Now we can pass my_callback_c to the C function

my_callback_c(42)

# This is the same as

my_callback(42)

# We can also pass my_callback_c to other Python functions

def my_other_callback(x, callback):
    print("my_other_callback called with", x)
    return callback(x)

my_other_callback(42, my_callback_c)

# This is the same as

my_other_callback(42, my_callback)
</code>

