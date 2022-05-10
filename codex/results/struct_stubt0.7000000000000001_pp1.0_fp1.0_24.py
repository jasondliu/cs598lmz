from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2i'  # little-endian int, int

# create binary file
with open('myfile.zip', 'wb') as f:
    f.write(b'\x50\x4B\x03\x04')
    f.write(s.pack(0x0a, 0x00))
    f.write(b'\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00')

# read binary file
with open('myfile.zip', 'rb') as f:
    data = f.read()

# unpack data
print(s.unpack(data[4:12]))

# unpack using the unpacked data
s = Struct('<2i')
print(s.unpack(data[4:12]))
