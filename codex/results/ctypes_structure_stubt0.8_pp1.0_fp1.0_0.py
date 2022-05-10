import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 5

S.__sizeof__()

a = S()
a

class NastyStruct(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int),
                ("pointer", ctypes.POINTER(None))
                ]

class T(object):
    def __init__(self):
        self.pointer = "foo"

t = T()
t.pointer

ref = NastyStruct()
ref.pointer = ctypes.pointer(t)
#
# ref.pointer.contents.pointer = "baz"
#
# ref.pointer.contents.pointer

#
# ctypes.c_bool
# ctypes.c_char
# ctypes.c_wchar
# ctypes.c_byte
# ctypes.c_ubyte
# ctypes.c_short
# ctypes.c_ushort
# ctypes.c_int
# ctypes.c_uint
# ctypes.c_long
# ctypes.c_ulong
# c
