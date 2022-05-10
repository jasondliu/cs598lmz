from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = 'I I I I'
s.size = s.calcsize(s.format)

fmt = Struct(s.format)

for i in range(5):
    rand_bytes = os.urandom(40)
    print(rand_bytes)
    bytes_out = fmt.pack(*rand_bytes)
    print(bytes_out)
    print(fmt.unpack(bytes_out))
    print(fmt.unpack_from(bytes_out, 0))
