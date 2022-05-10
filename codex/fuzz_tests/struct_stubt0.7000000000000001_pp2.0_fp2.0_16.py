from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# packed_data = s.pack('I 2s f', 1, 'ab'.encode('utf-8'), 2.7)
packed_data = s.pack(1, 'ab'.encode('utf-8'), 2.7)
packed_data

file_data = packed_data + b'xxxxxxxxxx'

data = s.unpack(file_data)
data

data = s.unpack_from(file_data, 4)
data

# The Struct class can also be used as a context manager

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = Struct('I 2s f').unpack_from(data, start)
    print(fields)
