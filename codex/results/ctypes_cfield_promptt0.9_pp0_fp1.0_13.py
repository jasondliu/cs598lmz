import ctypes
# Test ctypes.CField and ctypes.Field 

class x(ctypes.CStruct):
    _fields = [("x", ctypes.CField), ("reserved", ctypes.CField)]

print ctypes.sizeof(x)
print "ctypes.sizeof(ctypes.CField) * 2: ", ctypes.sizeof(ctypes.CField) * 2
