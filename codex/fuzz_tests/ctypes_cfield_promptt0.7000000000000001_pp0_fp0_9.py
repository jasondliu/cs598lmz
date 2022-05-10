import ctypes
# Test ctypes.CField

# Create a structure containing a CField
class CFieldStructure(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
    _anonymous_ = [('c', ctypes.c_int)]

# Create a structure containing a CField
class CFieldUnion(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
    _anonymous_ = [('c', ctypes.c_int)]

cfs = CFieldStructure()
print(cfs.a, cfs.b, cfs.c, cfs.d)
cfs.a = 10
cfs.b = 20
cfs.c = 30
print(cfs.a, cfs.b, cfs.c)
cfs.d = 40
print(cfs.a, cfs.b, cfs.c, cfs.d)

cfu = CFieldUnion()
print(cfu.a
