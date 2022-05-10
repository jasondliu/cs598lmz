import io
# Test io.RawIOBase
r = io.RawIOBase()
r.readinto1(bytearray(1))
r.readinto1(memoryview(bytearray(1)))
# Test io.BufferedIOBase
b = io.BufferedIOBase()
b.readinto1(bytearray(1))
b.readinto1(memoryview(bytearray(1)))
# Test BufferedReader
b = io.BufferedReader(io.BytesIO(b"abc"))
b.readinto1(bytearray(1))
b.readinto1(memoryview(bytearray(1)))
# Test BufferedWriter
b = io.BufferedWriter(io.BytesIO())
b.write(memoryview(b"abc"))
# Test FileIO
b = io.FileIO(__file__, mode="rb")
b.readinto1(bytearray(1))
b.readinto1(memoryview(bytearray(1)))
# Test BytesIO
b = io.BytesIO(b"abc")
b.readinto1(by
