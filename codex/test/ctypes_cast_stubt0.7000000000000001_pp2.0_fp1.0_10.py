import ctypes
ctypes.cast(None, ctypes.py_object)

import sys
sys.modules['_ctypes'] = sys.modules['ctypes']
del sys

del ctypes
