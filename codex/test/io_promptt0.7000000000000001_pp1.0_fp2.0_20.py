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
