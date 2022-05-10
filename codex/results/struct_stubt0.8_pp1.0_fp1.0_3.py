from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<h'
s.size = 2

def f(buf, offs):
    return s.unpack_from(buf, offs)

with open("memcached.txt", "wb") as f:
    f.write(b"a" * (2**20))

f("memcached.txt", 2**20)
