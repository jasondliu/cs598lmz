fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Issue #20226: sys.gettotalrefcount() should be callable
import sys
sys.gettotalrefcount()

# Issue #20295: PyLong_FromVoidPtr() should accept NULL pointer
import ctypes
ctypes.cast(None, ctypes.c_void_p)

# Issue #20302: PyModule_GetDict() should accept NULL pointer
ctypes.pythonapi.PyModule_GetDict.argtypes = (ctypes.py_object,)
ctypes.pythonapi.PyModule_GetDict(None)

# Issue #20303: PyImport_ImportModuleLevel() should accept NULL pointer
ctypes.pythonapi.PyImport_ImportModuleLevel.argtypes = (ctypes.c_char_p, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.c_int)
ctypes.pythonapi.PyImport_ImportModuleLevel(None, None, None, None, -1)

# Issue #20304: PyDict_GetItem() should accept NULL pointer
ctypes.
