import io
# Test io.RawIOBase

# Test that an instance of a subclass of RawIOBase can be created.
# (This tests the default implementations of the abstract methods.)
r = io.RawIOBase()

# Test that the default implementations work
r.close()
r.closed
r.fileno()
r.flush()
r.isatty()
r.readable()
r.read()
r.readinto(b"")
r.seek(0)
r.seekable()
r.tell()
r.truncate(0)
r.writable()
r.write(b"")

# Test that the default implementations of readinto() and write()
# raise io.UnsupportedOperation
try:
    r.readinto(b"")
except io.UnsupportedOperation:
    pass
else:
    raise RuntimeError("readinto() didn't raise io.UnsupportedOperation")

try:
    r.write(b"")
except io.UnsupportedOperation:
    pass
else:
    raise RuntimeError("write() didn't raise io.UnsupportedOperation")

# Test that the default
