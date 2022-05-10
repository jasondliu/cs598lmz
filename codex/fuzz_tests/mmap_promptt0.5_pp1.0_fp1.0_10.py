import mmap
# Test mmap.mmap.write
with open("test.txt", "w+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b"Hello world")
    m.write(b"foo")
    m.write(b"bar")
    m.write(b"baz")
    m.seek(0)
    assert m.read(5) == b"Hello"
    assert m.read(5) == b" worl"
    assert m.read(3) == b"dfo"
    assert m.read(3) == b"oba"
    assert m.read(3) == b"rba"
    assert m.read(3) == b"z"
    assert m.read(3) == b""
    m.close()
# Test mmap.mmap.read
with open("test.txt", "w+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b"Hello world")
    m.seek(0)
    assert
