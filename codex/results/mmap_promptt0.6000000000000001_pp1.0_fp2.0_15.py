import mmap
# Test mmap.mmap.read()
with open("dummy.txt", "w+") as f:
    m = mmap.mmap(f.fileno(), 0)
    # m.write(b"Hello world!")
    m.write(b"\x01\x02\x03\x04\x05")
    assert m.read(5) == b"\x01\x02\x03\x04\x05"
    m.seek(0)
    assert m.read(5) == b"\x01\x02\x03\x04\x05"
    assert m.read(5) == b""
    assert m.read(1) == b""
    assert m.read(0) == b""
    m.write(b"\x06\x07\x08\x09\x0a")
    m.seek(0)
    assert m.read(5) == b"\x01\x02\x03\x04\x05"
    assert m.read(5) == b"\x06\x07\x08
