import ctypes
# Test ctypes.CField
class CField(ctypes.CField):
    def __init__(self, type, offset, size=None, bit_offset=None, bit_size=None,
                 name=None, flags=None, doc=None):
        self.name = name
        self.type = type
        self.offset = offset
        self.size = size
        self.bit_offset = bit_offset
        self.bit_size = bit_size
        self.flags = flags
        self.doc = doc
    def __set__(self, instance, value):
        pass
    def __get__(self, instance, owner):
        pass
# Test ctypes.CField.from_address
class CFStruct(ctypes.Structure):
    pass
class CFType(ctypes.CStruct):
    pass
CFType._fields_ = [("a", ctypes.c_int),
                   CField("p",
                          ctypes.addressof(CFStruct),
                          size=ctypes.sizeof(CFStruct),
                          flags=ctypes.F_POINTER | c
