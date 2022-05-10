import _struct
# Test _struct.Struct.unpack()

s = _struct.Struct('i')
for big in 0, 1:
    s.bigendian = big
    for fmt in '@', '=', '<', '>':
        for integer in (-1, 0, 1, sys.maxsize, -sys.maxsize-1):
            packed = s.pack(integer)
            unpacked, = s.unpack(packed)
            assert unpacked == integer, (fmt, big, integer, unpacked)

# Test _struct.Struct.unpack_from()

data = b'abcd'

s = _struct.Struct('i')
for big in 0, 1:
    s.bigendian = big
    for fmt in '@', '=', '<', '>':
        for integer in (-1, 0, 1, sys.maxsize, -sys.maxsize-1):
            packed = s.pack(integer)
            unpacked, = s.unpack_from(packed, 0)
            assert unpacked == integer, (fmt, big, integer, unpacked)

