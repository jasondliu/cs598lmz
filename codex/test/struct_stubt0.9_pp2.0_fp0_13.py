from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
s.pack(b'123')

with open('arch.bin','wb') as f:
 f.write(b'holamundo')

with open('arch.bin','rb') as f:
 b = f.read()
print(b)

with open('arch.bin','rb') as f:
 b = f.read(3)
 print(b)
 b = f.read(4)
 print(b)

with open('arch.bin','rb') as f:
 b = f.read(8)
 print(b)
 b = f.read(8)
 print(b)

with open('arch.bin','rb') as f:
 b = f.read(4)
 print(b)
 f.seek(4)
 b = f.read(4)
 print(b)

f = open('arch.bin', 'rb')
f.tell()
#cambiar la posicion del puntero
