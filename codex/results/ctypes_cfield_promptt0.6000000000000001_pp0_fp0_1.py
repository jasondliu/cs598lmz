import ctypes
# Test ctypes.CField.from_address

import ctypes.test.test_cfield

class X(ctypes.LittleEndianStructure):
    _fields_ = [("a", ctypes.c_long),
                ("b", ctypes.c_long)]

class Y(ctypes.BigEndianStructure):
    _fields_ = [("a", ctypes.c_long),
                ("b", ctypes.c_long)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_long),
                ("b", ctypes.c_long)]

# Check that ctypes.CField.from_address works for LittleEndianStructure
# and BigEndianStructure, and fails for Structure.
c_void_p = ctypes.c_void_p

for cls in X, Y:
    addr = id(cls())
    field = ctypes.CField.from_address(addr, c_void_p, cls.a)
    assert field.offset == 0
    assert field.size == ctypes.
