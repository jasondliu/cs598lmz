import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
#
#  PyPy's ctypes
# ___________________________________________________________________________

# PyPy's ctypes is a simplified version of CPython's ctypes.
# It only supports the following subset of ctypes:
#
#  - c_int, c_uint, c_long, c_ulong, c_longlong, c_ulonglong
#  - c_float, c_double
#  - c_char, c_wchar, c_byte, c_ubyte, c_short, c_ushort
#  - c_char_p, c_wchar_p, c_void_p
#  - Structure, Union
#  - POINTER(T)
#  - CFUNCTYPE(restype, *argtypes)
#  - addressof, byref
#  - sizeof, alignment
#  - get_errno, set_errno
#  - get_last_error, set_last_error
#  - WinDLL, CDLL
#  - dlopen
