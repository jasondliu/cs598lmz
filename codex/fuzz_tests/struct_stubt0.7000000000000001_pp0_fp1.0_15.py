from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

# read the size of the data
with open(file, 'rb') as f:
    data = f.read(s.size)

# get the size
size = s.unpack(data)[0]
print(size)

# now read the data
with open(file, 'rb') as f:
    data = f.read(size)

print(data)
</code>

