import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class XX(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

# ctypes.CField has no __repr__ method yet, so we have to do it by hand
def CFieldRepr(self):
    return "CField(%s, %s, %d)" % (self.name, self.ctype, self.offset)
ctypes.CField.__repr__ = CFieldRepr

print("X._fields_")
for item in X._fields_:
    print("    %s" % item)
print("X.a")
print("    %s
