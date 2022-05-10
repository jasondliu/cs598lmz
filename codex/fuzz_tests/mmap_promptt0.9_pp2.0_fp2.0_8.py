import mmap
# Test mmap.mmap
m = mmap.mmap(-1, 1024, 'myfile', mmap.ACCESS_WRITE)
m.write('hello')
m.seek(0)

print repr(m.read(5))
print repr(m.read(1))
m.close()

import struct
# Test struct.pack
print repr(struct.pack('hhh', 1, 2, 3))
p 
