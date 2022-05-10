import ctypes
# Test ctypes.CField which is like a c_void_p but with a different name and doc
import _ctypes
test_lib = _ctypes.PyDLL(testlib)
CBar = ctypes.CField.in_dll(test_lib, 'bar')
CBar
CBar.__repr__(CBar)
CBar.__repr__.__doc__
CBar.value
# print the repr of a pointer-to-pointer:
tp = ctypes.POINTER(ctypes.c_int)
tp2 = ctypes.POINTER(tp)
repr(tp2)
t = tp2()
t
repr(t)

# Check if a CTypes object is a FFI pointer object:
ctypes.CData._is_ffi_pointer_type(ctypes.c_void_p)
# ... and pointers to pointers:
ctypes.CData._is_ffi_pointer_type(ctypes.POINTER(ctypes.c_void_p))

## Some more stuff to test the PyInterpreterState cache in _ctypes
#import sys
