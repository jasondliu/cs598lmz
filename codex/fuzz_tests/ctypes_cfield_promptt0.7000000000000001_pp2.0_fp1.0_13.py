import ctypes
# Test ctypes.CField...

def test(typ):
    p = ctypes.pointer(typ())
    print p[0].value
    p[0].value = 12
    print p[0].value

class B(ctypes.LittleEndianStructure):
    _fields_ = [("b", ctypes.c_ubyte)]

class C(ctypes.LittleEndianStructure):
    _fields_ = [("c", ctypes.c_ushort)]

class D(ctypes.LittleEndianStructure):
    _fields_ = [("d", ctypes.c_uint)]

class E(ctypes.LittleEndianStructure):
    _fields_ = [("e", ctypes.c_ulong)]

class F(ctypes.LittleEndianStructure):
    _fields_ = [("f", ctypes.c_ulonglong)]

class G(ctypes.LittleEndianStructure):
    _fields_ = [("g", ctypes.c_ubyte)]

class H(ctypes.LittleEndianStructure):
    _fields
