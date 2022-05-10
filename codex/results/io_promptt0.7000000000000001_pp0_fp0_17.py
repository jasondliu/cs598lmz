import io
# Test io.RawIOBase
# Read the three characters 'abc'.
r = io.RawIOBase()
r.readinto(bytearray(3))
