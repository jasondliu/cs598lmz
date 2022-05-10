import mmap
# Test mmap.mmap(fileno, > len(file), access=mmap.ACCESS_WRITE)
# test that it is still a view over some of the file.

with open('testfile', 'w+b') as f:
    f.write(b'This is a test')
    f.seek(0)
    m = mmap.mmap(f.fileno(), 100, access=mmap.ACCESS_WRITE)

    assert m[:] == b'This is a test'
    assert len(m) <= 100
    assert len(m) == len(b'This is a test')

import mmap
# Test mmap.mmap(fileno, 0, access=mmap.ACCESS_WRITE)
# test that it is still a view over the whole file.

with open('testfile', 'w+b') as f:
    f.write(b'This is a test')
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

