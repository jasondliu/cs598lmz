from _struct import Struct
s = Struct.__new__(Struct)
s.file = file
s.format = format
s.size = size = calcsize(format)
s.pack = lambda *x: file.write(s.pack_into(*x))
s.pack_into = lambda f, o, *x: f[o:o+size].__setitem__(0, s.pack(*x))
s.unpack = lambda f, o=0: s.unpack_from(f, o)[0]
s.unpack_from = lambda f, o=0: s.unpack(f[o:o+size], 0)
file.write(s.pack(139.5, 42, b"Fred"))
file.seek(0)
print(s.unpack(file.read(s.size)))
file.seek(0)
print(s.unpack_from(file.read()))
