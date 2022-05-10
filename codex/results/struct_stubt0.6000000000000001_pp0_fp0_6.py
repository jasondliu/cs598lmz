from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>c2s2s3s3s3s3s')
print(s.size)
print(s.pack(b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07'))
