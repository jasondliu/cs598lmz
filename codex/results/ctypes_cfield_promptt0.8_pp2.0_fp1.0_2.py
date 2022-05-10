import ctypes
# Test ctypes.CField

fields = [('a', ctypes.c_char),
          ('b', ctypes.c_short),
          ('c', ctypes.c_int),
          ('d', ctypes.c_long),
          ('e', ctypes.c_char),
          ('f', ctypes.c_short),
          ('g', ctypes.c_char)]

# Reference
class C(ctypes.Structure):
    _fields_ = fields

class CField(ctypes.CField):
    def __init__(self, *args):
        ctypes.CField.__init__(self, *args)
        self.select = self.align = self.size = 0

class D(ctypes.Structure):
    _fields_ = [CField(*field) for field in fields]

print("Reference:")
print("Alignment:", C._pack_, C.size)
for field in C._fields_:
    name, type = field
    print("%10s %10s %10d %10x %10d" % (name, type
