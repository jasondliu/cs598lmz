import ctypes
# Test ctypes.CFUNCTYPE()

# This is the prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the function that will be called
@CALLBACKFUNC
def callback(a, b):
    print("callback called with %d and %d" % (a, b))
    return a + b

# This is the function that will call the callback
def caller(f, a, b):
    print("caller called with %d and %d" % (a, b))
    return f(a, b)

# Call the caller
print(caller(callback, 2, 3))
</code>
It prints:
<code>caller called with 2 and 3
callback called with 2 and 3
5
</code>

