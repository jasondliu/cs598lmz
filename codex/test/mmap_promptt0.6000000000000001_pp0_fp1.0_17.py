import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 13)
m.write(b"Hello, world!")
m.seek(0)
assert m.read(13) == b"Hello, world!"
m.close()
# Test mmap.mmap() with a file descriptor
with tempfile.TemporaryFile() as tf:
    m = mmap.mmap(tf.fileno(), 13)
    m.write(b"Hello, world!")
    m.seek(0)
    assert m.read(13) == b"Hello, world!"
    m.close()
# Test mmap.mmap() with a file object
with tempfile.TemporaryFile() as tf:
    m = mmap.mmap(tf, 13)
    m.write(b"Hello, world!")
    m.seek(0)
    assert m.read(13) == b"Hello, world!"
    m.close()
# Test mmap.mmap() with a negative length
