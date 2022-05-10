import ctypes
# Test ctypes.CField types.

# c_int_fields is an array of c_int typed fields
class c_int_fields(ctypes.Structure):
    _fields_ = [("field%d" % i, ctypes.c_int) for i in range(10)]

# c_char_fields is an array of c_char typed fields
class c_char_fields(ctypes.Structure):
    _fields_ = [("field%d" % i, ctypes.c_char) for i in range(10)]

# c_wchar_fields is an array of c_wchar typed fields
class c_wchar_fields(ctypes.Structure):
    _fields_ = [("field%d" % i, ctypes.c_wchar) for i in range(10)]

# c_ubyte_fields is an array of c_ubyte typed fields
class c_ubyte_fields(ctypes.Structure):
    _fields_ = [("field%d" % i, ctypes.c_ubyte) for i in range(10)]


