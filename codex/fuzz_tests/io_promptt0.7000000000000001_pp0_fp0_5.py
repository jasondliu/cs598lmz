import io
# Test io.RawIOBase
if (False):
    f = io.RawIOBase()
    f.name
    f.mode
    f.closed
    f.close()
    f.closed
    f.isatty()
    f.fileno()
    f.seekable()
    f.readable()
    f.writable()
    f.read(2)
    f.readinto(bytearray(3))
    f.readinto(bytearray(3), 1)
    f.readinto(bytearray(3), 1, 2)
    f.readall()
    f.write(b"hello")
    f.seek(2)
    f.seek(2, 0)
    f.seek(10, 1)
    f.seek(10, 2)
    f.tell()
    f.truncate()
    f.truncate(10)


# Test io.BufferedIOBase
if (False):
    f = io.BufferedIOBase()
    f.raw
    f.detach()
    f.detach
