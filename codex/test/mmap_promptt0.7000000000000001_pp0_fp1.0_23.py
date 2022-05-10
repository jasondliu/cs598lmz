import mmap
# Test mmap.mmap()

f = open('/tmp/memmap', 'w+b')
f.write(b'\x00' * mmap.ALLOCATIONGRANULARITY)
m = mmap.mmap(f.fileno(), 0)
m[0:11] = b'Hello World'
m.close()
f.close()

m = mmap.mmap(-1, mmap.ALLOCATIONGRANULARITY)
m.close()

print('mmap.mmap() test passed')

# Test mmap.mmap(0)

f = open('/tmp/memmap', 'w+b')
f.write(b'\x00' * mmap.ALLOCATIONGRANULARITY)
m = mmap.mmap(f.fileno(), 0)
m[0:11] = b'Hello World'
m.close()
f.close()

m = mmap.mmap(0, mmap.ALLOCATIONGRANULARITY)
