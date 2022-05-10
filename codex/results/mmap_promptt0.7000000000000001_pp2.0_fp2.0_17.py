import mmap
# Test mmap.mmap
# mmap.mmap(fileno, length, flags, prot, access, offset)
f = open('mmap.txt', 'r+')
m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_WRITE)
m.write('0123456789abcdef')
m.seek(0)
print(m.read(16))
m.close()
f.close()
