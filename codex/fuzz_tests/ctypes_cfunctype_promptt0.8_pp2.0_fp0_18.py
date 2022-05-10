import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

# void (int, int)
func = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(
    _ctypes_test.struct_callbacks.callback)
s = _ctypes_test.struct_callbacks()
s.callback = func
s.method_callback = func
s.call(1, 2)
s.method_call(1, 2)

# void ()
func = ctypes.CFUNCTYPE(None)(lambda: None)
s = _ctypes_test.struct_callbacks()
s.callback = func
s.method_callback = func
s.call(1, 2)
s.method_call(1, 2)
