import ctypes
# Test ctypes.CFUNCTYPE()
# define a callback function to be used with CFUNCTYPE
@ctypes.CFUNCTYPE(None)
def hello_func():
    print("Hello, World!")

# obtain a function pointer to the callback
