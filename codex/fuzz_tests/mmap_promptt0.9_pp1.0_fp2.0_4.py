import mmap
# Test mmap.mmap()
m = mmap.mmap(6, 555, 'a')
m.write(b'First - Last')
m.close()

# Test mmap.mmap()
m = mmap.mmap(6, 555, 'b')
m.write(b'Hello world')
m.seek(0)
print(m.readline())
m.close()
