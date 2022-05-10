import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
It returns <code>&lt;__main__.LP_PyObject object at 0x0000000002A2D848&gt;</code>
I expect to have a string <code>hello</code> as the output.
What am I doing wrong?


A:

There are some interactions between the ctypes foreign function interface and Python functions.  
The ctypes FFI creates a Python means of calling a foreign function (or a Python extension module function, etc.), which then calls your Python function.  That is, Python needs to call your Python function, and it uses the <code>CFUNCTYPE</code> Python foreign function interface to do that.  But, it also needs to understand that calling the Python function needs to return a result to the foreign calling context.
<code>In [6]: ctypes.CFUNCTYPE(cint)(lambda : 42)()                                                                
Out[6]: 42
</code>
So, to return a Python string from C, we need an FFI that understands the Python object protocol for a string, which is a little more
