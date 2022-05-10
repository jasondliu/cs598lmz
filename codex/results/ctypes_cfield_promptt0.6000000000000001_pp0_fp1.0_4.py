import ctypes
# Test ctypes.CField
class record(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_long),
                ("c", ctypes.c_char*8)]

print(record.a)
print(repr(record.b))
print(record.c)

print(record.a.offset)
print(record.a.size)
print(record.a.index)
print(record.a.type)
print(record.a.name)
print(record.a.pack)

print(record.a.offset)
print(record.b.offset)
print(record.c.offset)

print(record.a.size)
print(record.b.size)
print(record.c.size)

print(record.a.index)
print(record.b.index)
print(record.c.index)

print(record.a.type)
print(record.b.type)
print(record.c.type)

print(record.a.name)

