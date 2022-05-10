import io
# Test io.RawIOBase
# Test io.RawIOBase.readinto
def test_rawiobase_readinto():
    buf = bytearray(10)
    r = io.RawIOBase()
    with raises(io.UnsupportedOperation):
        r.readinto(buf)

# Test io.RawIOBase.write
def test_rawiobase_write():
    r = io.RawIOBase()
    with raises(io.UnsupportedOperation):
        r.write(b"1234")

# Test io.FileIO
def test_fileio():
    f = io.FileIO(__file__)
    assert f.mode == "rb"
    # assert f.seekable() is True
    assert f.readable() is True
    assert f.writable() is False
    assert f.name == __file__
    assert f.close() is None
    assert f.closed is True
    assert f.read(1) == b""

# Test io.FileIO.write
def test_fileio_write():
    f = io.FileIO(__file
