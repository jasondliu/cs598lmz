import mmap
# Test mmap.mmap()
# TEST_VALUE = b"I'm a little mmapped string!"

# with open('/tmp/mmaptest', 'w+b') as f:
#     f.write(TEST_VALUE)
#     f.seek(0)
#     m = mmap.mmap(f.fileno(), len(TEST_VALUE))
#     print(m[:])
#     m.seek(0)
#     m.write(b"I'm a little byte string!")
#     m.seek(0)
#     print(m.read(1))
#     m.close()

# Test mmap.mmap(fileno, length, tagname, access=mmap.ACCESS_DEFAULT)

TEST_VALUE = b"I'm a little mmapped string!"

with open('/tmp/mmaptest', 'wb') as f:
    f.write(TEST_VALUE)

