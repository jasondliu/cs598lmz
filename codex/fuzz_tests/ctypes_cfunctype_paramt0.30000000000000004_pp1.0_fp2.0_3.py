import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def _callback(a, b):
    print('callback called')
    return a + b

callback = FUNTYPE(_callback)

# Create a new C++ instance
obj = cpp.MyClass()

# Set the callback
obj.set_callback(callback)

# Call the callback
result = obj.call_callback(1, 2)
print('result:', result)

# Delete the C++ instance
del obj
</code>

