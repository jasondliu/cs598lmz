import mmap
# Test mmap.mmap()

f = open('/dev/mem', 'r+b')
m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0x80000000)

value = m.read(4)
print(value)

m.seek(0)
m.write(b'\x00\x00\x00\x00')

m.seek(0)
value = m.read(4)
print(value)

m.close()
f.close()

print('end')

# Test mmap.mmap()

f = open('/dev/mem', 'r+b')
m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0x80000000)
