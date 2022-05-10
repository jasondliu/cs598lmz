import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte()
    y = ctypes.c_ubyte()
    z = ctypes.c_ubyte()

class U(ctypes.Union):
    _fields_ = [("a", ctypes.c_char * 1),
                ("b", S)]

print(S(), U().b, U().a)

#S(_0=0, _1=0, _2=0) S(_0=0, _1=0, _2=0) bytearray(b'\x00')
