import io
# Test io.RawIOBase
with io.BytesIO() as f:
    f.write(b"hello")
    f.seek(0)
    assert f.read() == b"hello"
    assert f.read() == b""

with io.BytesIO(b"hello") as f:
    assert f.read() == b"hello"
    assert f.read() == b""

with io.BytesIO(b"hello") as f:
    assert f.seek(0, io.SEEK_CUR) == 0
    assert f.seek(2, io.SEEK_CUR) == 2
    assert f.seek(0, io.SEEK_CUR) == 2
    assert f.seek(0) == 0
    assert f.seek(2) == 2
    assert f.seek(0, io.SEEK_CUR) == 2
    assert f.seek(-1, io.SEEK_END) == 4
    assert f.seek(0, io.SEEK_END) == 5
    assert f.seek(0, io.SEEK_END) == 5

