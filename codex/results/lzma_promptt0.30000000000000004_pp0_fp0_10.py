import lzma
# Test LZMADecompressor.decompress() with a file object
# that has a read() method that returns a bytes object.

data = b"x" * 1000000
compressed = lzma.compress(data)

class MyBytesIO(io.BytesIO):
    def read(self, n=-1):
        return super().read(n)

with MyBytesIO(compressed) as f:
    d = lzma.LZMADecompressor()
    assert d.decompress(f) == data
# Test LZMADecompressor.decompress() with a file object
# that has a read() method that returns a bytearray object.

data = b"x" * 1000000
compressed = lzma.compress(data)

class MyBytesIO(io.BytesIO):
    def read(self, n=-1):
        return bytearray(super().read(n))

with MyBytesIO(compressed) as f:
    d = lzma.LZMADecompressor()
    assert d.decompress(
