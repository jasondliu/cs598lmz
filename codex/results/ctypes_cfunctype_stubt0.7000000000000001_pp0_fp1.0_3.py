import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

fun.__name__ = "fun"

import sys
_module = ctypes.PyDLL(sys.executable)

_module.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.py_object), ctypes.c_char_p, ctypes.py_object, ctypes.c_int]
_module.Py_InitModule4.restype = ctypes.py_object

_module.Py_InitModule4("foo", None, "", None, 1013)

from foo import fun
</code>
...but this still raises the same exception. How do I get the module to see the function?


A:

The problem is that you are using the wrong API. You are using <code>Py_InitModule4</code>, which is the Python 2 API. You are running Python 3.
To create a module in Python 3, use the <code>PyModule_Create</code> function. The documentation is here.
<code>from ctypes import *
from _ctypes
