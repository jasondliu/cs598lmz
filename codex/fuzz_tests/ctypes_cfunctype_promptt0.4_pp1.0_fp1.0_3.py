import ctypes
# Test ctypes.CFUNCTYPE

# These are the standard types that are available for use
# with CFUNCTYPE.
#
#  c_char
#  c_wchar
#  c_byte
#  c_ubyte
#  c_short
#  c_ushort
#  c_int
#  c_uint
#  c_long
#  c_ulong
#  c_longlong
#  c_ulonglong
#  c_float
#  c_double
#  c_char_p
#  c_wchar_p
#  c_void_p

# This is an example of a callback function.
def py_callback(x):
    print("py_callback:", x)
    return x

# This is an example of a callback function with a
# different signature.
def py_callback2(x, y):
    print("py_callback2:", x, y)
    return x + y

# This is an example of a callback function with a
# different signature.
def py_callback3(x, y, z
