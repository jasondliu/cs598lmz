from _struct import Struct
s = Struct.__new__(Struct)
s._fmt = '>16H'
data = open('myfile.bin', 'rb').read()
print(s.unpack_from(data))

# allows a "raw" format, which is an alternate syntax for specifying byteorder,
# standard size, and alignment
s = Struct('raw', '>16H')
print(s.size)

# debug output with field names
s = Struct('h l q f d s c x')
for name, typ in s._fields:
    print('%4s: %s' % (name, typ))

# calculate padding bytes
print(s.size, s.alignment)
print(s.pack_into(b'', 0, 1, 2, 3, 4, 5, 6, b'A', b'B'))
print(s.size)
