from _struct import Struct
s = Struct.__new__(Struct)
msg = 'a'*10
s.format = '<%iH'
msg, arg = s._compile(s.format, 114)
out = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\x0d\x0e\x0f'
s, result = s._unpack_iter(msg, arg, out)
result = list(result)
"{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}{:6x}".format(*result)
'''
# python3.1-32 Struct_bug.py 
#out: 
#0x0001 0x0203 0x0405 0x0607 0x0809 0x0a0b 0x0c0d 0x0e0f 0x0000 0x0000 0x0000
