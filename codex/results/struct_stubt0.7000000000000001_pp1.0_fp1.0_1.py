from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = calcsize(s.format)

print('Format string  :', s.format)
print('Uses           :', s.size, 'bytes')
print('Packed Value   :', s.pack(*(7, b'xy', 2.7)))

print('Unpacked Value :', s.unpack(b'\x07\x00\x00\x00xy\x00\x00\x9a\x99\x99\x99\x99\x9a'))
