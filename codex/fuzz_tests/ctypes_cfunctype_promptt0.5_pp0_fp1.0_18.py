import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_void_p

import ctypes

# A ctypes callback
def my_callback(arg1, arg2):
    print "my_callback called with arguments:", arg1, arg2
    return 42

# Get a void pointer to the callback
callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
my_callback_ptr = callback_type(my_callback)
my_callback_void_ptr = ctypes.cast(my_callback_ptr, ctypes.c_void_p)

# Call the callback
print "Calling the callback..."
print my_callback_ptr(1, 2)

# Call the callback through the void pointer
print "Calling the callback through the void pointer..."
print ctypes.cast(my_callback_void_ptr, callback_type)(1, 2)
</code>
The output is as follows:
<code>Calling the callback...
my_callback called with arguments: 1 2
42
Calling the callback through the void pointer...
my_
