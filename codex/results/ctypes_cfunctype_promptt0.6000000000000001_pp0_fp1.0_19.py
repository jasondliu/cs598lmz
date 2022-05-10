import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda x:x*x)(2) == 4

# 1. Defining a callback function
def py_callback(msg, length):
    print "Message:", msg
    return length

# 2. The callback function must have the prototype of a function
#    that has two arguments and returns an int.
#    The arguments are a pointer to a string and an int.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

# 3. The callback function must be converted to a function pointer
#    with the same prototype.
#    The function pointer is passed as an argument to the DLL function.
callback = CMPFUNC(py_callback)

# 4. Call the DLL function.
#    The function pointer is passed as an argument.
#    The function pointer is converted to a void pointer
#    by ctypes before it is passed to the DLL function.
dll.cpp_function(ctypes.c_void_p(callback))

#
