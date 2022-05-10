from _struct import Struct
s = Struct.__new__(Struct)
fmt = b'!HHL1'
data = 'aaaa'
# s.unpack(fmt, data)
# Traceback (most recent call last):
# File "<stdin>", line 225, in <module>
# TypeError: unpack() argument 1 must be a string argument
s.unpack(fmt, bytes(data, 'utf-8'))
# (3457, 1, 1574, b'a')
s.pack(fmt, 1, 2, 3, 4)
# b'\x00\x01\x00\x02\x00\x00\x0b\x04'
s.unpack(fmt, bytes.fromhex('00010002000b04'))
# (1, 2, 3, 4)
