from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">I"
fmt = s.pack_forever()
def eq(a, b):
    assert a == b, "%r != %r" % (a, b)
eq(fmt.size, 4)
eq(fmt.alignment, 4)
eq(fmt.pack(99), b'\x00\x00\x00c')
eq(fmt.unpack(b'\x00\x00\x00c')[0], 99)
eq(fmt.pack(99), b'\x00\x00\x00c')

# check that error handling is based on the first character
s.format = ">II"
fmt = s.pack_forever()
eq(fmt.size, 8)
eq(fmt.alignment, 8)
eq(fmt.pack(99), b'\x00\x00\x00c\x00\x00\x00\x00')
eq(fmt.unpack(b'\x00\x00\x00c')[0],
