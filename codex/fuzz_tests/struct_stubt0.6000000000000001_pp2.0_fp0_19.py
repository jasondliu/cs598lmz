from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(s.unpack(header))
del header
del s

# The struct module is not needed to unpack, but it is helpful to see what is being unpacked

# memoryview is used to save memory when unpacking.
# Rather than create a new byte object, memoryview creates a new view of the existing data.
