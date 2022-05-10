import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
The error message is:
<code>Process finished with exit code -1073741819 (0xC0000005)
</code>
This is the same error message I get when I try to run the <code>ctypes.CFUNCTYPE</code> example in the Python documentation.
Note that the above code works in Python 2.7.
I'm using Python 3.5.1 on Windows 7.

