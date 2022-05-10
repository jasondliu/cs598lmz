import lzma
# Test LZMADecompressor on a string
data = open('test.xz', 'rb').read()
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(data)
len(result)

# Test LZMADecompressor on a file-like object
data = open('test.xz', 'rb')
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(data)
len(result)

# Test LZMADecompressor.decompress() on a file-like object
# that raises an exception
class BrokenFile:
    def read(self, size):
        raise OSError

data = BrokenFile()
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(data)
except OSError:
    pass
else:
    raise Exception("Expected an exception")

# Test LZMADecompressor on a file-like object
data = open('test.xz', 'rb')
