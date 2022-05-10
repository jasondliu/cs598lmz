import ctypes
# Test ctypes.CField from extensible structs
#https://docs.python.org/3/library/ctypes.html#extending-and-embedding-ctypes
class ExtendedStructure(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

    @classmethod
    def from_param(cls, obj):
        if isinstance(obj, tuple):
            return cls(*obj)
        elif isinstance(obj, cls):
            return obj
        raise TypeError("Cannot convert %s to %s" % (obj, cls))

class BasicStructure(ctypes.Structure):
    EXTENDED_FIELD = ExtendedStructure(1)

    _fields_ = [("i", ctypes.c_int),
                ("ext", EXTENDED_FIELD)]

print(BasicStructure(1, 2))
print(BasicStructure.EXTENDED_FIELD)
print(BasicStructure(1, ExtendedStructure(3)))

#error
#print(BasicStructure(1, 3))


# Test ctypes.PyCSimpleType
