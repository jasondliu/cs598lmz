import io
# Test io.RawIOBase.
with open("/dev/null", "rb") as f:
    io.RawIOBase.writable(f)
    io.RawIOBase.readable(f)
