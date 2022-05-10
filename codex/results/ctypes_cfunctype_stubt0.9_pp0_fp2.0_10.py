import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world"

result = mod.my_function(fun)
print result
</code>
Note that I am printing the result of the ffi call in Python. I pass a function to the C function and that function returns a Python object. So automatically there will be an FFI call. This is the same as what you would need in C.
The reason it is even possible to pass a function is because the underlying calling convention is standard C/Windows. This means that the called function can itself call functions that accept callbacks.

