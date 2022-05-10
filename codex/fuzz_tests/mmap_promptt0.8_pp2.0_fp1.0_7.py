import mmap
# Test mmap.mmap by creating a file with the known length and going past it
# to test that the C code handles that correctly.
with open(TESTFN, 'w+b') as f:
    f.write(b'q\r\nq\r\n')
with open(TESTFN, 'r+b') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:
        assert m.read(1) == b'q'
        assert m.readline() == b'q\r\n'
        assert m.readline(5) == b'q\r\n'
        assert m.readline(4) == b''
        assert m.read(1) == b''
        # Small buffer test
        m.seek(0)
        buf = m.read(2)
        assert len(buf) == 2
        m.write(b"xy")
        m.seek(0)
        buf = m.read(2)
        assert buf == b"xy"
        # Test that
