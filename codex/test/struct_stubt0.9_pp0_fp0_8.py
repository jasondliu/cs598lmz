from _struct import Struct
s = Struct.__new__(Struct)
msg = 'a'*10
s.format = '<%iH'
msg, arg = s._compile(s.format, 114)
out = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\x0d\x0e\x0f'
s, result = s._unpack_iter(msg, arg, out)
result = list(result)
"{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}".format(*result)
