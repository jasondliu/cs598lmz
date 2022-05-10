import _struct
# Test _struct.Struct
s = _struct.Struct("hhQQ")
s.size
s.size = 7
s.size
s.pack(1, 2, 3, 4)
s.unpack(_struct.pack("hhQQ", 1, 2, 3, 4))
_struct.calcsize("hhQQ")
try:
    s.pack(1)
except TypeError as err:
    print(err)
try:
    s.unpack(b'aaa')
except _struct.error as err:
    print(err)
b = _struct.pack("i", 1)[0:3]
try:
    _struct.unpack("i", b)
except _struct.error as err:
    print(err)
s = _struct.Struct("hi")
s.size
s.size = 3
s.size
s.pack(1, 2)
s.unpack(_struct.pack("hi", 1, 2))
_struct.calcsize("hi")
