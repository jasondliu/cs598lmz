import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 1024)
m.write(b'Hello World')
m.seek(0)
print(m.read(11))
m.close()

# Test mmap.mmap(fileno, length)
f = open('/etc/passwd', 'r+')
m = mmap.mmap(f.fileno(), 1024)
m.write(b'Hello World')
m.seek(0)
print(m.read(11))
m.close()

# Test mmap.mmap(fileno, length, tagname)
f = open('/etc/passwd', 'r+')
m = mmap.mmap(f.fileno(), 1024, 'test')
m.write(b'Hello World')
m.seek(0)
print(m.read(11))
m.close()

