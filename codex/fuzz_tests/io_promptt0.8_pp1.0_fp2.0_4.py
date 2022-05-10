import io
# Test io.RawIOBase

try:
    io.RawIOBase
except AttributeError:
    import sys
    print >> sys.stderr, "SKIP"
    raise SystemExit

# Test general functionality
fp = io.BytesIO()
fp.write(b"foo")

fp = io.BytesIO(b"foo")
assert fp.read() == b"foo"
assert fp.read(1) == b"f"
assert fp.readable()
assert not fp.writable()
assert not fp.seekable()

fp.tell()
fp.truncate()
fp.fileno()
fp.tell()
fp.readinto(bytearray(1))
fp.readinto(memoryview(bytearray(1)))

# Test io.RawIOBase.read1()
fp = io.BytesIO(b"foo")
assert fp.read1(1) == b"f"
assert fp.read1() == b"oo"

# Test error conditions
fp = io.BytesIO()
try:
    fp.
