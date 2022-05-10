import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
I get the following error:
<code>TypeError: function takes exactly 0 arguments (1 given)
</code>
I'm using Python 2.7.3 on Mac OS X 10.8.2.


A:

You can use <code>ctypes.c_void_p</code> to represent <code>void *</code> and then cast it to a function pointer.  This works for me:
<code>import ctypes

def void_fun():
    pass

fun_pointer = ctypes.cast(ctypes.c_void_p.from_address(id(void_fun)),
                          ctypes.CFUNCTYPE(None))
</code>

