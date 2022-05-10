from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)

f = open('data.bin', 'rb')

data = f.read(s.size)
print(s.unpack(data))

f.close()

# Writing a binary file

from _struct import Struct
s = Struct('I 2s f')

with open('data.bin', 'wb') as f:
    data = s.pack(1, b'ab', 2.7)
    f.write(data)

# Reading a binary file using a higher-level approach

with open('data.bin', 'rb') as f:
    data = f.read()
    print(s.unpack(data))

# Reading a binary file in chunks

with open('data.bin', 'rb') as f:
    for chunk in iter(lambda: f.read(20), b''):
        print(chunk)

# Writing binary data to a file

import array

nums = array.array('i', [1,
