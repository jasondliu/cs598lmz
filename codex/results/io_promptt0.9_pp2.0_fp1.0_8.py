import io
# Test io.RawIOBase
def test_rawiobase(obj):
    io.RawIOBase.readline(obj)
    io.RawIOBase.read1(obj)
    io.RawIOBase.readinto(obj, Uninitialize)
    io.RawIOBase.readinto1(obj, Uninitialize)
    io.RawIOBase.read(obj, 100)
    io.RawIOBase.readall(obj)
    io.RawIOBase.write(obj, "ab")
    io.RawIOBase.writelines(obj, [bytes(range(256))])
    io.RawIOBase.detach(obj)
    io.RawIOBase.fileno(obj)
    assert io.RawIOBase.isatty(obj)
    io.RawIOBase.tell(obj)
    io.RawIOBase.seek(obj, 100)
    io.RawIOBase.seek(obj, 0, os.SEEK_SET)
    assert io.RawIOBase.readable(obj)
    assert not io.RawIOBase.seekable(obj)
    assert io
