import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]
</code>
That works fine.
But if I change the return type to <code>ctypes.c_int</code>:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return [1,2,3]
</code>
I get the following error:
<code>TypeError: don't know how to convert Python return value type 'list' to C return value type 'int'
</code>
I would like to be able to use <code>ctypes.c_int</code> as the return type and still be able to return a list. Is that possible?


A:

You can't return a list, but you can return a pointer to a list.
<code>import ctypes

def fun():
    return [1,2,3]

FUNTYPE = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))
fun_ptr = FUNTYPE(fun)

print(fun_ptr()
