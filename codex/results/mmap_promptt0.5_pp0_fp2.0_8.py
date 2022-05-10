import mmap
# Test mmap.mmap
with open("test_mmap.txt", "w+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b"Hello world!")
    assert mm.read(1) == b"H"
    assert mm.read(6) == b"ello w"
    assert mm.read(1) == b"o"
    assert mm.read(1) == b"r"
    assert mm.readline() == b"ld!"
    mm.seek(0)
    assert mm.readline() == b"Hello world!"
    mm.close()
# Test mmap.mmap with a size
with open("test_mmap.txt", "w+b") as f:
    mm = mmap.mmap(f.fileno(), 12)
    mm.write(b"Hello world!")
    assert mm.read(1) == b"H"
    assert mm.read(6) == b"ello w"
    assert mm.read(1) == b"o"
    assert mm.read(
