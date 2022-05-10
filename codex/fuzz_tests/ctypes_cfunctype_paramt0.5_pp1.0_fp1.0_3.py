import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

def hello_callback(i):
    print("hello from callback", i)

# Convert the Python callback into a C callback
c_callback = FUNTYPE(hello_callback)

# Call the C function, which will call our Python callback
lib.call_callback(c_callback)

# Call the C function, which will call our Python callback
lib.call_callback(c_callback)

# Call the C function, which will call our Python callback
lib.call_callback(c_callback)

# Call the C function, which will call our Python callback
lib.call_callback(c_callback)

# Call the C function, which will call our Python callback
lib.call_callback(c_callback)
