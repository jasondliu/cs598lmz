import io
# Test io.RawIOBase.readinto()
assert isinstance(io.FileIO(__file__, 'r').readinto(bytearray()), int)
# Test io.BufferedIOBase.readinto()
assert isinstance(io.BufferedReader(io.FileIO(__file__, 'r')).readinto(bytearray()), int)
# Test io.TextIOBase.readinto()
