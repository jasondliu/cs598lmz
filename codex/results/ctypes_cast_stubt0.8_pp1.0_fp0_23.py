import ctypes
ctypes.cast(ptr, ctypes.py_object).value
</code>
Usually <code>ctypes</code> shouldn't be used in Python because it can cause crashes and other problems.
But in this case, it is one of the only (optionally) portable ways to get the internal pointer.

In CPython, you can also use:
<code>int(ptr) # or long(ptr)
</code>
but this is not portable to other Python implementations like Jython, IronPython and PyPy.

On PyPy, you can also use the <code>rffi</code> module:
<code>import sys
from rpython.rlib import rffi

def Py_int(ptr):
    return rffi.cast(rffi.INT, ptr)

def Py_long(ptr):
    return rffi.cast(rffi.LONG, ptr)

# etc.
</code>

