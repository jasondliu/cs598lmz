import io
# Test io.RawIOBase

# Test read()
r = io.RawIOBase()
try:
    r.read()
except io.UnsupportedOperation:
    pass
else:
    print('io.RawIOBase.read() did not raise UnsupportedOperation')

# Test readall()
try:
    r.readall()
except io.UnsupportedOperation:
    pass
else:
    print('io.RawIOBase.readall() did not raise UnsupportedOperation')

# Test readinto()
try:
    r.readinto(bytearray(10))
except io.UnsupportedOperation:
    pass
else:
    print('io.RawIOBase.readinto() did not raise UnsupportedOperation')

# Test readinto() with a memoryview
try:
    r.readinto(memoryview(bytearray(10)))
except io.UnsupportedOperation:
    pass
else:
    print('io.RawIOBase.readinto() did not raise UnsupportedOperation')

# Test read1()
try:
    r.read1()
except io.UnsupportedOperation
