import _struct
# Test _struct.Struct("ii")

# ints from 0 to 255
print("ints from 0 to 255")
for i in range(256):
    for j in range(256):
        s = _struct.Struct("ii")
        data = s.pack(i,j)
        print("%i %i %r" % (i, j, data))
        print("%i %i" % s.unpack(data))

# ints from 0 to 65535
print("ints from 0 to 65535")
for i in range(65536):
    for j in range(65536):
        s = _struct.Struct("ii")
        data = s.pack(i,j)
        print("%i %i %r" % (i, j, data))
        print("%i %i" % s.unpack(data))

# ints from -128 to 127
print("ints from -128 to 127")
for i in range(-128, 127):
    for j in range(-128, 127):
        s = _struct.Struct("ii")
        data = s.pack(i
