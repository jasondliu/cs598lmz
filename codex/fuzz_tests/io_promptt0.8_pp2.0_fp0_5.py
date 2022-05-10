import io
# Test io.RawIOBase

# Test constructor
reader = io.RawIOBase()
try:
    reader.fileno()
except io.UnsupportedOperation:
    pass
else:
    print("fileno() without fileno() should raise UnsupportedOperation")

reader = io.RawIOBase(open(TESTFN, "rb"))
reader.fileno()

# Test invalid constructor call
try:
    io.RawIOBase(42)
except TypeError:
    pass
else:
    print("integer constructor should raise TypeError")

# Test read/readall/readinto
with open(TESTFN, "rb") as f:
    data = f.read()

reader = io.RawIOBase(open(TESTFN, "rb"))
got = reader.read()
if got != data:
    print("readall with read() mismatch")

reader = io.RawIOBase(open(TESTFN, "rb"))
got = reader.read(-1)
if got != data:
    print("readall with read(-1) mismatch")

reader = io.RawIOBase(
