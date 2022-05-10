import io
# Test io.RawIOBase properties by using a real file.
with io.IOBase.open(__file__, mode="rb") as f:
    assert f.mode == "rb"
    assert f.fileno() is not None
    assert f.readable()
    assert not f.writable()
    assert f.seekable()
    assert f.tell() == 0
    assert f.read(64) == open(__file__, "rb").read(64)
    assert f.tell() == 64
    assert f.seek(0, io.SEEK_SET)
    assert f.seek(0, io.IOBase.SEEK_SET) == 0
    assert f.tell() == 0
    assert f.seek(-1, io.SEEK_END) == os.fstat(f.fileno()).st_size - 1
    assert f.tell() == os.fstat(f.fileno()).st_size - 1
    assert f.seek(1, io.SEEK_CUR) == os.fstat(f.fileno()).st_size
    assert f.tell()
