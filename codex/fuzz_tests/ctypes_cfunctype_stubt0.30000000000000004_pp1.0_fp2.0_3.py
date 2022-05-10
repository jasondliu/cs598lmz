import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

fun()
</code>
This works and returns 'hello'. But if I try to return a list, it fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ['hello']

fun()
</code>
This fails with:
<code>TypeError: cannot be converted to a pointer
</code>
If I try to pass a list to the function, it also fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg

fun(['hello'])
</code>
This fails with:
<code>TypeError: cannot be converted to a pointer
</code>
How can I pass lists to and from C functions?


A:

You need to use <code>ctypes.py_object</code> instead of <code>ctypes.c_void_p</code>.
<code
