import io
# Test io.RawIOBase
wrapper = io.BufferedReader(io.BytesIO(b"abcde"))
underlying = wrapper.raw
assert isinstance(underlying, io.BytesIO)
assert underlying.readinto(bytearray(2)) == 2
assert underlying.readinto(bytearray(4)) == 3
