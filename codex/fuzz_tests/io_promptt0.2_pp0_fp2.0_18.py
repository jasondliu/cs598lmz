import io
# Test io.RawIOBase

# Test RawIOBase.read()

# Test read() with 0 bytes
r = io.RawIOBase()
r.read(0)

# Test read() with positive bytes
r = io.RawIOBase()
r.read(1)

# Test read() with negative bytes
r = io.RawIOBase()
r.read(-1)

# Test read() with None bytes
r = io.RawIOBase()
r.read(None)

# Test read() with non-integer bytes
r = io.RawIOBase()
r.read(1.0)

# Test RawIOBase.readinto()

# Test readinto() with 0 bytes
r = io.RawIOBase()
r.readinto(bytearray(0))

# Test readinto() with positive bytes
r = io.RawIOBase()
r.readinto(bytearray(1))

# Test readinto() with negative bytes
r = io.RawIOBase()
r.readinto(bytearray(-1))

# Test readinto() with None
