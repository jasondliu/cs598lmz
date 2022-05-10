import ctypes
# Test ctypes.CField.
#
class Struct1(ctypes.LittleEndianStructure):
    _fields_ = [ ctypes.CField("val", ctypes.c_int), ]

obj = Struct1()
print obj.val
# Test to asseure all formatchar work as expected
#
class FormatStruct(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("c", ctypes.c_char),
        ("b", ctypes.c_byte),
        ("h", ctypes.c_short),
        ("i", ctypes.c_int),
        ("l", ctypes.c_long),
        ("f", ctypes.c_float),
        ("d", ctypes.c_double),
        ("P", ctypes.c_void_p),
    ]
obj = FormatStruct()

# Test alignment
#
class AlignmentStruct(ctypes.BigEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("b", ctypes.c_byte),
        ("c", c
