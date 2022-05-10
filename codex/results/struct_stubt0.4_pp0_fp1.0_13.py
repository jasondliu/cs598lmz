from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s'
s.size = s.calcsize(s.format)
s.pack_into(buf, 0, 'foo')
print buf

# s.pack_into(buf, 0, 'foobar') # ValueError: unpack requires a string argument of length 3

s.pack_into(buf, 0, 'foobar') # ValueError: unpack requires a string argument of length 3

print buf

buf = bytearray(s.size)
s.pack_into(buf, 0, 'foo')
print buf

buf = bytearray(s.size)
s.pack_into(buf, 0, 'foobar') # ValueError: unpack requires a string argument of length 3

print buf

buf = bytearray(s.size)
s.pack_into(buf, 0, 'foobar') # ValueError: unpack requires a string argument of length 3

print buf
