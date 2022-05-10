from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('!B')

with open('test.bin', 'rb') as f:
    data = f.read()

for i in range(0, len(data), s.size):
    buffer = data[i:i+s.size]
    value = s.unpack(buffer)[0]
    print(value)
