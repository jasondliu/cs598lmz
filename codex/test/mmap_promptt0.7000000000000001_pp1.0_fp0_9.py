import mmap
# Test mmap.mmap(-1, 5)
# m = mmap.mmap(-1, 5)
# print(m[:])
# m.close()

# Test mmap.mmap(0, 5)
with open('t.txt', 'w') as f:
    f.write('hello')
with open('t.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m.close()

# Test mmap.mmap(0, 5, access=mmap.ACCESS_WRITE)
with open('t.txt', 'w') as f:
    f.write('hello')
with open('t.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m[:])
    m[:] = b'12345'
    m.close()
    f.seek(0)
    print(f.read())

# Test mmap.
