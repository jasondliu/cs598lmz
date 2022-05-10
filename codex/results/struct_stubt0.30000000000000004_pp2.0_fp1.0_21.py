from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<2s3s')
s.unpack(b'\x01\x02\x03\x04\x05')

# _struct.Struct.unpack(b'\x01\x02\x03\x04\x05')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unpack() missing 1 required positional argument: 'buffer'

# _struct.Struct.unpack(b'\x01\x02\x03\x04\x05', b'\x01\x02\x03\x04\x05')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unpack() takes 2 positional arguments but 3 were given

# _struct.Struct.unpack(b'\x01\x02\x03\x04\x05', b'\x01\x02\x03\x04\x05', b'\x01\x02\x
