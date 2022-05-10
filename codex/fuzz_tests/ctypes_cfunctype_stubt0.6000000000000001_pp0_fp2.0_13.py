import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hi"
print fun()

# Make a function object
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hi"

# Register it with the interpreter
import _ctypes
_ctypes.PyDLL.PyDict_SetItemString(_ctypes.PyEval_GetBuiltins(), "fun", fun)

# Call it
print fun()

import _ctypes

# Note that the function only has to be registered once.

# Get the builtin dict
builtins = _ctypes.PyDLL.PyDict_New()

# Get the builtin module
import sys
builtin_module = sys.modules["__builtin__"]

# Get the builtin dict from the module
_ctypes.PyDLL.PyObject_SetAttrString(builtins, "__builtins__", builtin_module.__dict__)

# Register the function
_ctypes.PyDLL.PyDict_SetItemString(builtins, "fun
