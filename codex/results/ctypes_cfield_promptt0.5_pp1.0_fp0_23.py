import ctypes
# Test ctypes.CField

# Create a CField in a structure
class CFieldStruct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]

# Create a CField in a union
class CFieldUnion(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]

# Create a CField in a class
class CFieldClass(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]

# Test a CField in a structure
cs = CFieldStruct()
cs.a = 1
cs.b = 2
print(cs.a, cs.b)

# Test a CField in a union
cu = CFieldUnion()
cu.a = 1
print(cu.a, cu.b)

# Test a CField in a class
cc = CFieldClass()
cc.a = 1
cc.b = 2
print(cc
