import mmap
# Test mmap.mmap
mm = mmap.mmap(-1, 30)
mm.seek(0)
mm.write(b'0123456789abcdef')
mm.seek(0)
print(mm.read(10))

# Test mmap.mmap(fileno)
f = open('/dev/zero', 'rb')
mm = mmap.mmap(f.fileno(), 0)
mm.seek(0)
mm.write(b'0123456789abcdef')
mm.seek(0)
print(mm.read(10))

# Test mmap.mmap(fileno, length)
f = open('/dev/zero', 'rb')
mm = mmap.mmap(f.fileno(), 100)
mm.seek(0)
mm.write(b'0123456789abcdef')
mm.seek(0)
print(mm.read(10))

# Test mmap.mmap(fileno, length, offset)
f = open('/dev/zero', 'rb')
mm = mmap.mmap(f.fil
