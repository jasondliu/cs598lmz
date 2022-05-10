import ctypes
# Test ctypes.CField
if ctypes.sizeof(ctypes.CField) != ctypes.sizeof(ctypes.c_void_p) * 2:
    raise Exception("ctypes.CField is not correct")

# Test ctypes.Structure
class TestStructure(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]

if ctypes.sizeof(TestStructure) != ctypes.sizeof(ctypes.c_int):
    raise Exception("ctypes.Structure is not correct")

# Test ctypes.Union
class TestUnion(ctypes.Union):
    _fields_ = [("value", ctypes.c_int)]

if ctypes.sizeof(TestUnion) != ctypes.sizeof(ctypes.c_int):
    raise Exception("ctypes.Union is not correct")

# Test ctypes.Array
class TestArray(ctypes.Array):
    _fields_ = [("value", ctypes.c_int)]

if ctypes.sizeof(TestArray) != ctypes.sizeof(ctypes
