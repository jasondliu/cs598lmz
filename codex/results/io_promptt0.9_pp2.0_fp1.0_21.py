import io
# Test io.RawIOBase is a type
assert issubclass(io.RawIOBase, type)
s = io.BytesIO()
s.close()
assert s.closed

# Issue #4970: Check that io.StringIO() works with unicode
io.StringIO(u"abc")

# Issue 15865: Check that io.StringIO() explicitly forbids bytes
try:
    io.StringIO(b"abc")
except TypeError:
    pass
else:
    assert False, "bytes are erroneously accepted by io.StringIO."

# Issue #5874: recursive function calls in io.FileIO.read().
with open(test_support.TESTFN, "wb") as f:
    f.write(b"abcd" * 10)
with open(test_support.TESTFN, "rb") as f:
    f.read()
with open(test_support.TESTFN, "rb") as f:
    f.read(1024)
with open(test_support.TESTFN, "rb") as f:
    f.read(0)
with open(test
