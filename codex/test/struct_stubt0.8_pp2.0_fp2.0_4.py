from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

pack('I 2s f', 1, 'ab', 2.7)
pack('>I 2s f', 1, 'ab', 2.7)
pack('<I 2s f', 1, 'ab', 2.7)


unpack('>I 2s f', b'\x00\x00\x00\x01ab\x00\x00\x00')

fmt = '<3s 3s HH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())
header = img[:10]
bytes(header)

unpack(fmt, header)
del header
del img
