import io
# Test io.RawIOBase

# Test RawIOBase.read()
r = io.RawIOBase()
try:
    r.read()
except io.UnsupportedOperation:
    pass
else:
    print("io.RawIOBase.read() didn't raise UnsupportedOperation")

# Test RawIOBase.readinto()
try:
    r.readinto(b"")
except io.UnsupportedOperation:
    pass
else:
    print("io.RawIOBase.readinto() didn't raise UnsupportedOperation")

# Test RawIOBase.write()
try:
    r.write(b"")
except io.UnsupportedOperation:
    pass
else:
    print("io.RawIOBase.write() didn't raise UnsupportedOperation")

# Test RawIOBase.seek()
try:
    r.seek(0)
except io.UnsupportedOperation:
    pass
else:
    print("io.RawIOBase.seek() didn't raise UnsupportedOperation")

# Test RawIOBase.tell()
try:
    r.tell()
except io.UnsupportedOperation:
