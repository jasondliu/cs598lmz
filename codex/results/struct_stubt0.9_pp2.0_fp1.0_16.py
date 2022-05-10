from _struct import Struct
s = Struct.__new__(Struct)
s.pack_into = lambda fmt, buf, ofs, *args: buf.write(fmt.pack(*args))
s.unpack_from = Struct.unpack_from

fmt = Struct('I 2s f')
with open('data.b', 'wb') as f:
    s.pack_into('Iif', f, 0, 1, b'xy', 3.14)
    s.pack_into('2si', f, 10, b'AB', 42)
f = open('data.b', 'rb')
print(s.unpack_from(fmt, f))
print(s.unpack_from(fmt, f, 10))
