import ctypes
# Test ctypes.CField
class Test(ctypes.Union):
    _fields_ = [("a", ctypes.c_uint16),
                ("b", ctypes.c_uint16, 5),
                ("c", ctypes.c_uint16, 5),
                ("d", ctypes.c_uint16, 6)]

print(Test.a.offset)
print(Test.b.offset)
print(Test.c.offset)
print(Test.d.offset)

print(Test.a.size)
print(Test.b.size)
print(Test.c.size)
print(Test.d.size)

print(Test.a.bits)
print(Test.b.bits)
print(Test.c.bits)
print(Test.d.bits)

print(Test.a.length)
print(Test.b.length)
print(Test.c.length)
print(Test.d.length)

print(Test.a.type)
print(Test.b.type)
print(Test.c.type)
print(Test.d.type
