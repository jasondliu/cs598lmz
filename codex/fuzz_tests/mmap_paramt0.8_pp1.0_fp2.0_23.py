import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()


mm = mmap.mmap(-1, 1, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0, 0)

print(mm)

mm.write('1')
mm.seek(0)
print(mm.read(5))

mm.close()
