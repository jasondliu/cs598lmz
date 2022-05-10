import io
# Test io.RawIOBase
with io.BytesIO(b'Hello\n') as f:
    f.read(10)
    f.tell()
    f.seek(0)
    f.read()
    f.tell()
    f.seek(-1, io.SEEK_CUR)
    f.tell()
    f.seek(0)
    f.tell()
    f.read()
    f.flush()
    f.seek(0)
    f.tell()
    f.tell()
    f.read()
    f.close()
    assert not f.closed
    f.tell()
    with pytest.raises(ValueError):
        f.seek(-1)
with io.BytesIO() as f:
    assert not f.writable()
with io.BytesIO() as f:
    assert f.seekable()
with io.BytesIO() as f:
    assert not f.readable()
with io.BytesIO() as f:
    assert not f.isatty()
with io.BytesIO() as f:
    assert not f.fil
