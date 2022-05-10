import _struct
# Test _struct.Struct(b'=i')
print("Test _struct.Struct(b'=i')")
s = _struct.Struct(b'=i')
try:
	for i in range(0, 256):
		bs = chr(i) * s.size
		print("%02x ==> %d, %d, %d" %(i, s.unpack(bs), s.unpack_from(bs, 0),
			s.unpack_from(bs, 1)))
		#print("%02x ==> %s" %(i, repr(s.unpack(bs))))
except _struct.error as e:
	print("Exception: %s" %(e,))

# Test _struct.Struct(b'!i')
print("Test _struct.Struct(b'!i')")
s = _struct.Struct(b'!i')
