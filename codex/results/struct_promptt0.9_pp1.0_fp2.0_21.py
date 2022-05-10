import _struct
# Test _struct.Struct with one element format string.
_struct.Struct('f').pack(1.2)
_struct.Struct('d').pack(1.2)
_struct.Struct('l').pack(1)
_struct.Struct('q').pack(1)
_struct.Struct('i').pack(1)
_struct.Struct('h').pack(1)
_struct.Struct('c').pack(1)
_struct.Struct('b').pack(1)
# TypeError is not raised because 1.2
# is converted to '1' as an integer
_struct.Struct('b').pack(1.2)
# Test Issue #11718:
import _ctypes
_struct.Struct("").pack(b"")
_struct.Struct("").pack(bytearray())
_struct.Struct("").pack(_ctypes.c_char())
_ctypes.c_char().value
_struct.Struct("").pack(_ctypes.c_buffer(""))
# TypeError is raised because c_char object
# does not have attribute value
_struct.Struct("").pack(_ctypes.c_
