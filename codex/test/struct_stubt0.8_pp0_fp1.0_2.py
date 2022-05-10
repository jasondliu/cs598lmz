from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__init__(">IIQQQQQQ")
print(s)
print(s.size)
print(s.format)
print(s.pack(1, 2, 3, 4, 5, 6, 7, 8))
print(s)
print(s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x08'))
print(s)

# Stream IO
print("Stream IO")
from io import BytesIO
s = BytesIO()
print(s)
s.write(b'binary data')
