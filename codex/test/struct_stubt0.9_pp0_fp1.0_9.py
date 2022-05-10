from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>i'
s.size = calcsize('>i')
p = s.pack(42)  # b'\x00\x00\x00\x2a'
print(p)
print(p.size)   # 4
print(p.format) # b'\x00\x00\x00\x2a'
print(p.format[0]) # 0

print(b'\x00\x00\x00\x2a')==b'\x00\x00\x00*' #  False
print(struct.pack(">i", 42))
print(b'\x00\x00\x00\x2a')

