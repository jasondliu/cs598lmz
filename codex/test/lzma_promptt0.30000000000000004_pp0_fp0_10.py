import lzma
# Test LZMADecompressor.decompress() with a file object
# that has a read() method that returns a bytes object.

data = b"x" * 1000000
compressed = lzma.compress(data)

