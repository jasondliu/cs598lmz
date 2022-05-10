from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">2h2i"
s.size = s.calcsize()

s = Struct(">ffff") #> verifica o endereço de memoria do sistema que a constante está alocada.

s.pack(4, 5.4, 6, 7)



# _struct.error: ushort format requires -32768 <= number <= 32767

print(s.unpack(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00'))
