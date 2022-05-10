import _struct
# Test _struct.Struct
import struct
import sys

# Test the alignment of the structs
for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(fmt)
    assert s.size == struct.calcsize(fmt)
    assert s.alignment == struct.calcsize('x' + fmt) - struct.calcsize(fmt)

# Test pack/unpack
for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(fmt)
    for i in range(0, 256):
        for j in range(0, 256):
            packed = s.pack(i, j)
            unpacked = s.unpack(packed)
            assert len(unpacked) == 2
            assert unpacked[0] == i
            assert unpacked[1] == j

# Test pack
