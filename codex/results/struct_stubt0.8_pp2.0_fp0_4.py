from _struct import Struct
s = Struct.__new__(Struct)
s.fmt = b"<2i2f"
s.size = calcsize(s.fmt)

def unpack(data):
    n = len(data) // s.size
    for i in range(n):
        p = s.unpack_from(data, i * s.size)
        print(p)

def pack(data):
    l = []
    for d in data:
        l.append(s.pack(*d))
    return b"".join(l)

b = pack([[0, 1, 2.0, 3.0], [4, 5, 6.0, 7.0]])
print(b)
unpack(b)

b = pack([[0, 1, 2.0, 3.0], [4, 5, 6.0, 7.0], [8, 9, 10.0, 11.0]])
print(b)
unpack(b)
