from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hif')
print(s.pack(1,2,3))
print(s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00'))

#struct.unpack_from(fmt, buffer, offset=0)
#struct.pack_into(fmt, buffer, offset, v1, v2, ...)
#struct.calcsize(fmt)

#struct.pack_into(fmt, buffer, offset, v1, v2, ...)
#struct.unpack_from(fmt, buffer, offset=0)
import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))
del header
del img
