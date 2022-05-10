import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the callback function
# int CALLBACK MyCallback(int x, int y);
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the prototype of the function we are calling
# int MyFunction(int x, int y, int (CALLBACK *callback)(int, int));
