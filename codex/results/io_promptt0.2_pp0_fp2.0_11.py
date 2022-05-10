import io
# Test io.RawIOBase

# Test RawIOBase.read()

# Test read() with 0 bytes
r = io.RawIOBase()
r.read(0)

# Test read() with negative size
try:
    r.read(-1)
except ValueError:
    pass
else:
    print('Failed to raise ValueError')

# Test read() with positive size
try:
    r.read(1)
except NotImplementedError:
    pass
else:
    print('Failed to raise NotImplementedError')

# Test RawIOBase.readall()

# Test readall()
try:
    r.readall()
except NotImplementedError:
    pass
else:
    print('Failed to raise NotImplementedError')

# Test RawIOBase.readinto()

# Test readinto()
try:
    r.readinto(bytearray(1))
except NotImplementedError:
    pass
else:
    print('Failed to raise NotImplementedError')

# Test RawIOBase.readinto()
