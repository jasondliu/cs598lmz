import ctypes
# Test ctypes.CField
# ctypes.CField types also have a _type_ attribute
import _ctypes_test
ctypes.CField(_ctypes_test.Union1, "a")._type_ is ctypes.c_int
ctypes.CField(_ctypes_test.Union1, "a")._type_ is ctypes.c_short
ctypes.CField(_ctypes_test.Union2, "b")._type_ is ctypes.c_ubyte
ctypes.CField(_ctypes_test.Struct1, "a")._type_ is ctypes.c_int
ctypes.CField(_ctypes_test.Struct1, "b")._type_ is ctypes.c_short
ctypes.CField(_ctypes_test.Struct2, "b")._type_ is ctypes.c_ubyte
# Test ctypes.c_void_p and ctypes.c_char_p
if sizeof(ctypes.c_char) == sizeof(ctypes.c_byte):
    ctypes.c_void_p(b"123").value
    ctypes.
