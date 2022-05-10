from _struct import Struct
s = Struct.__new__(Struct)
print(s)

s.__init__('!I 2s f')
print(s)

## r = s.pack(1, b'ab', 3.0)
## print(s.size)
## print(s.format)
## print(s.unpack(r))
## print(s.unpack(r))

#
# get init
#


from _struct import Struct

s = Struct('!I 2s f')
print(s.format, s.size, s.pack(1, b'ab', 3.0), s.unpack(b'\x01ab@'))
