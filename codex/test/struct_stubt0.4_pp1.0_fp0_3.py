from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

with open('data.bin', 'wb') as f:
    f.write(s.pack(1, b'ab', 2.7))

with open('data.bin', 'rb') as f:
    data = f.read()

