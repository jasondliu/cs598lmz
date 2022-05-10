import _struct
# Test _struct.Struct with standard format characters
# and standard size/alignment.

import _struct

s = _struct.Struct('cbhilfd?')
print s.size
print s.pack('x', -127, -32767, -2147483647L, -9223372036854775807L,
	   1.0, 2.0, True)
print s.unpack(s.pack('x', -127, -32767, -2147483647L, -9223372036854775807L,
		      1.0, 2.0, True))

# Test big-endian format characters
s = _struct.Struct('>cbhilfd?')
print s.size
print s.pack('>', -127, -32767, -2147483647L, -9223372036854775807L,
	   1.0, 2.0, True)
print s.unpack(s.pack('>', -127, -32767, -2147483647L, -9223372036854775807
