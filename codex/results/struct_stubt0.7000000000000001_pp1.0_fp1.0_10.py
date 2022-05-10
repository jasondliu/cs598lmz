from _struct import Struct
s = Struct.__new__(Struct)
print s.format
print s.size
s.format = "i"
print s.size
print s.unpack(b'\x01\x00\x00\x00')
print s.pack(1)

# print __builtins__.__dict__

# from _struct import _clearcache
# _clearcache()

print Struct.__doc__
print Struct.__new__.__doc__
print Struct.__init__.__doc__
print Struct.__new__.__doc__
print Struct.__reduce_ex__.__doc__
print Struct.__reduce__.__doc__
print Struct.__reduce_ex__.__doc__
print Struct.format_token.__doc__
print Struct.format.__doc__
print Struct.unpack_from.__doc__
print Struct.unpack.__doc__
print Struct.pack_into.__doc__
print Struct.pack.__doc__
print Struct.iter_unpack.__doc__
print Struct.size.__doc__
print Struct.alignment.__
