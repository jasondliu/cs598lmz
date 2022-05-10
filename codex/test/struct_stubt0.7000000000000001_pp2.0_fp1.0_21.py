from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update({'format': 'hhl', 'size': 8})

# Create an instance of the Struct class
s = Struct('hhl')

# Use the new instance to pack an argument list
packed_data = s.pack(b'ab', b'cd', 1)

# Accessing attributes from the new instance
print('format  :', s.format)
print('size (bytes)  :', s.size)

# Unpacking the data with the same format
print(s.unpack(packed_data))

# Using iter_unpack()
for rec in s.iter_unpack(b'abcdabcd'):
    print(rec)

# Using unpack_from()
print(s.unpack_from(b'abcdabcd', 4))

# Converting between integers and float
from _struct import pack, unpack

print(unpack('>f', pack('>l', 6917529027641081856)))

# Accessing attributes from the Struct class
from _struct import Struct
