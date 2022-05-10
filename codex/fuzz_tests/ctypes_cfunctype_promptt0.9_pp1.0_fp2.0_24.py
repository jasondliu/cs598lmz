import ctypes
# Test ctypes.CFUNCTYPE, ctypes.POINTER, ctypes.stdcall
# These objects should be imported from ctypes, as in a real
# application.
CFUNCTYPE = ctypes.CFUNCTYPE
POINTER = ctypes.POINTER
stdcall = ctypes.stdcall
# The wrapped function is in a real library, test lib. It's not in a library.
function = ctypes.WINFUNCTYPE(None)
f = function(("test", lib.test))
f()
