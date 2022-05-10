import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

# TypeError: 'CFUNCTYPE' object is not callable
</code>
I've also tried using <code>ctypes.WINFUNCTYPE</code> instead of <code>ctypes.CFUNCTYPE</code>, but that doesn't work either.
How can I create a function that returns a string?


A:

You need to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>

