import io
# Test io.RawIOBase

# io.RawIOBase.readinto()
with io.BytesIO() as f:
    assert f.readinto(bytearray(1)) == 0
