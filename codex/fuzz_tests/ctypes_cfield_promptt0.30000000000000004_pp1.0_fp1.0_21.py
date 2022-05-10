import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

print X.a.offset
print X.a.size
print X.a.index
print X.a.name
print X.a.ctype
print X.a.type
print X.a.bitsize
print X.a.bitoffset
print X.a.readonly
print X.a.pack
print X.a.alignment

print X.b.offset
print X.b.size
print X.b.index
print X.b.name
print X.b.ctype
print X.b.type
print X.b.bitsize
print X.b.bitoffset
print X.b.readonly
print X.b.pack
print X.b.alignment

print X.a.offset == X.b.offset

x = X()
x.a = 1
x.b = 2
print x.a
print
