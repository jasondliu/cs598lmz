import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
This works, but I would like to be able to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>. However, this does not work:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
It gives the error <code>TypeError: must be string without null bytes, not str</code>.
I have also tried <code>ctypes.c_char_p(b"hello")</code> and <code>ctypes.c_char_p(u"hello")</code> but they both give the same error.
How can I return a string from a function that is defined using <code>ctypes.CFUNCTYPE</code>?


A:

The <code>ctypes.CFUNCTYPE</code> function takes a <code>restype</code> argument. This argument should be the
