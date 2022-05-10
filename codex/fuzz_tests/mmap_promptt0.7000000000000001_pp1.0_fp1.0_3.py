import mmap
# Test mmap.mmap()

memmap_file = 'test.bin'
with open(memmap_file, 'w+b') as f:
    f.write(b'\x00' * 10)
    memmap_obj = mmap.mmap(f.fileno(), 0)
    memmap_obj.write(b'Hello World!')
    print 'memmap_obj =', memmap_obj[:]
    print 'memmap_obj.size() =', memmap_obj.size()
    memmap_obj.seek(0)
    print 'After memmap_obj.seek(0): memmap_obj.read(5) =', memmap_obj.read(5)
    print 'memmap_obj.tell() =', memmap_obj.tell()
    memmap_obj.close()
# Test mmap.mmap(-1, length)

import mmap

memmap_file = 'test.bin'
with open(memmap_file, 'w+b') as f:
    f.write(b'\x00' * 10)
    mem
