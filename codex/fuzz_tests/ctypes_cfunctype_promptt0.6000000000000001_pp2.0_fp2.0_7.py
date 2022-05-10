import ctypes
# Test ctypes.CFUNCTYPE
def foo(a, b, c):
    return a + b + c

def callback(a, b, c):
    print("callback called")
    return a + b + c

# Create a callback function prototype
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create a callback function
mycallback = CALLBACKFUNC(callback)

# Call foo with mycallback as the callback function
print(foo(1, 2, 3, callback=mycallback))

# Call foo with callback as the callback function
print(foo(1, 2, 3, callback=callback))

# Call foo with no callback function
print(foo(1, 2, 3))

# Call foo with None as the callback function
print(foo(1, 2, 3, callback=None))

# Call foo with a string as the callback function
try:
    print(foo(1, 2, 3, callback="not a function"))
except Exception as e:
   
