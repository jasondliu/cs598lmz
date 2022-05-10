from _struct import Struct
s = Struct.__new__(Struct)
print(type(s))
print('='*100)

# 下面示例将结构体类型和缓冲区类型结合
from _ctypes import Structure
from _ctypes import byref
from _ctypes import c_bool
from _ctypes import c_long
from _ctypes import c_longlong
from _ctypes import c_ubyte
from _ctypes import c_uint16
from _ctypes import c_ulonglong
from _ctypes import c_void_p
from _ctypes import pointer
from binascii import hexlify

