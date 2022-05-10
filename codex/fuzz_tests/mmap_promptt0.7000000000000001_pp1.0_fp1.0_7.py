import mmap
# Test mmap.mmap() for the second argument.
with open("data/sample.txt", "w+") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b"abcdefghijklmnopqrstuvwxyz")
    m.seek(0)
    assert m.read(1) == b"a"
    assert m.read(4) == b"bcde"
    assert m.read(1) == b"f"
with open("data/sample.txt", "w+") as f:
    m = mmap.mmap(f.fileno(), 100)
    m.write(b"abcdefghijklmnopqrstuvwxyz")
    m.seek(0)
    assert m.read(1) == b"a"
    assert m.read(4) == b"bcde"
    assert m.read(1) == b"f"
with open("data/sample.txt", "w+") as f:
    m = mmap.mmap(f.fileno(), 0
