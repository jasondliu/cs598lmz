import io
# Test io.RawIOBase.
with open("/dev/null", "rb") as f:
    io.RawIOBase.writable(f)
    io.RawIOBase.readable(f)
    f.write(b"abc")
    f.seek(0)
    f.tell()
    f.read(3)
with open("/dev/null", "wb") as f:
    io.RawIOBase.writable(f)
    io.RawIOBase.readable(f)
    f.write(b"abc")
    f.seek(0)
    f.tell()
    f.read(3)
# Test io.BufferedIOBase.
with open("/dev/null", "rb") as f:
    io.BufferedIOBase.writable(f)
    io.BufferedIOBase.readable(f)
    f.write(b"abc")
    f.seek(0)
    f.tell()
    f.read(3)
with open("/dev/null", "wb") as f:
    io.BufferedIOBase.writable
