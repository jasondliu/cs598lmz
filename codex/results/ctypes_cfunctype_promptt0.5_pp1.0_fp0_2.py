import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the callback function
# int CALLBACK MyCallback(int x, int y);
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the prototype of the function we are calling
# int MyFunction(int x, int y, int (CALLBACK *callback)(int, int));
MyFunction = ctypes.CDLL("test.dll").MyFunction
MyFunction.argtypes = [ctypes.c_int, ctypes.c_int, CALLBACK]
MyFunction.restype = ctypes.c_int

# This is the callback function
def MyCallback(x, y):
    print x, y
    return x + y

# Calling the function
print MyFunction(1, 2, MyCallback)
</code>

