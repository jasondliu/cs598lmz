import mmap
# Test mmap.mmap file access on Windows
o = open('/tmp/mmap_test', 'wb')
map = mmap.mmap(o.fileno(), 0)
map.write(r'\x00\x01\x02\x03\x04')
map.seek(0,0)
for i in range(5):
    if ord(map.read(1)) != i:
        print 'read error'
map.seek(3,0)
if ord(map.read(1)) != 3:
    print 'read error'
map.close()
o.close()
