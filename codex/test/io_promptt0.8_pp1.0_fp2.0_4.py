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
