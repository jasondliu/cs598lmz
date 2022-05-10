from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')

with open('t1.bin', 'wb') as f:
    f.write(s.pack(3))
    f.write(s.pack(17))
    f.write(s.pack(450))

with open('t1.bin', 'rb') as f:
    print(f.read(s.size))
