import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but it seems like a lot of work. Is there a way to do this without having to define a new function type?


A:

You can use <code>ctypes.cast</code> to cast a function pointer to a Python function.
<code>import ctypes

def fun():
    return "hello"

fun_ptr = ctypes.cast(fun, ctypes.c_void_p).value

print(fun_ptr)
</code>

