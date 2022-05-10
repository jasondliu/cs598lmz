from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I 4s')
s.size

s.pack(808, b'hello')

s.unpack(b'\x04\xd2\x04\x0chello')

s.unpack_from(b'\x04\xd2\x04\x0chello world', 2)

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):  # show the first 3 file headers
    start += 14
    fields = Struct('<IIIHH').unpack_from(data, start)
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size  # skip to the next header
