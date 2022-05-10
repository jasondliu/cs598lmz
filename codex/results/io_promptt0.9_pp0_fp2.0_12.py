import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase
# Test io.StringIO
# Test io.BytesIO
# Test io.BufferedReader
# Test io.BufferedWriter
# Test io.BufferedRWPair
# Test io.BufferedRandom
# Test io.FileIO
# Test io.TextIOWrapper
# Test io.StringIO

TestError = "io.unsupportedOperation"

# test readinto() is implemented
bytes_list = [bytes([1, 2, 3]), bytes([4, 5, 6])]
for bytes_item in bytes_list:
    class TestRawIO(io.RawIOBase):
        def readinto(self, b):
            b[:] = bytes_item
            return len(bytes_item)

    rawio = TestRawIO()
    buf = bytearray(len(bytes_item)+10)
    result = rawio.readinto(buf[10:])
    assert result == len(bytes_item) and bytes(buf[10:]) == bytes_item

# test readinto()
