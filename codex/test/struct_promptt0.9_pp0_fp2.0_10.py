import _struct
# Test _struct.Struct.pack_into
import binascii

s = _struct.Struct('bxxxc')
bytes = buffer('a' * s.size)
s.pack_into(bytes, 0, *(1,), 'd')
