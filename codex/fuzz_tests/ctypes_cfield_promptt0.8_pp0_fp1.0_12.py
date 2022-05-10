import ctypes
# Test ctypes.CFields
ctypes.CFields


class TestStruct(ctypes.Structure):
    _fields_ = (("x", "i"), ("y", "d"))


class TestUnion(ctypes.Union):
    _fields_ = (("x", "i"), ("y", "d"))


class TestStructureWithPointerField(ctypes.Structure):
    _fields_ = (("x", "i"), ("next", TestStruct))


class TestStructureWithArrayField(ctypes.Structure):
    _fields_ = (("x", "i", 3),)


class TestStructureWithBitField(ctypes.Structure):
    _fields_ = (("x", "i", 3), ("y", "i", 5), ("z", "i", 8))


class TestStructureWithVoidPointer(ctypes.Structure):
    _fields_ = (("x", "i"), ("p", "P"))


class TestStructureWithCharPointer(ctypes.Structure):
    _fields_ = (("x", "i"), ("p", "s
