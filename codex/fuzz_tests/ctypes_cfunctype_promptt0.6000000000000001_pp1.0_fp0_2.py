import ctypes
# Test ctypes.CFUNCTYPE

# The following function uses a function pointer to access a function in a
# shared library.

# On Mac OS X, it seems that the linker doesn't export the symbol unless
# it's actually used, so we need to use it from here.
from ctypes.test import need_symbol

if hasattr(ctypes, 'c_wchar'):
    unicode_type = unicode
else:
    unicode_type = str

class X(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]

Xp = ctypes.POINTER(X)

# On Windows, functions in a DLL are exported with the stdcall calling
# convention, on Unix they are exported with the C calling convention.
if sys.platform == "win32":
    stdcall_func = ctypes.WINFUNCTYPE
else:
    stdcall_func = ctypes.CFUNCTYPE

@stdcall_func(Xp, ctypes.c_int)
def funcptr_test(x, value):
    x.cont
