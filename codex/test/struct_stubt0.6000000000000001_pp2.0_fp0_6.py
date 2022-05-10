from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i4sh')
s.size

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = s.unpack_from(data, start)
    crc32, comp_size, uncomp_size = fields

    start += s.size
    filename = data[start:start+comp_size]
    start += comp_size
    print(filename)
