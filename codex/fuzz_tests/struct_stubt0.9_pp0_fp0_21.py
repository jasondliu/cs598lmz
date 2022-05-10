from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = b'<3s3sHH'
b = bytes([119,119,119,0,0,0,0,0,0,0,0,0])
try:
	data = s.unpack(b)
except:
	import sys
	print(sys.exc_info()[1])
	raw_input()
print(data)
print(b'WWW\x00\x00')
print(b.de
