from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<3s3sHH"
s.size = calcsize(s.format)
print(s.size)

def iter_unpack(format, data):
    s = Struct.__new__(Struct)
    s.format = format
    s.size = calcsize(s.format)
    for offset in range(0, len(data), s.size):
        yield s.unpack_from(data, offset)

with open("/tmp/myfile.zip", "rb") as f:
    for header in iter_unpack("<3s3sHH", f.read()):
        print(header)
