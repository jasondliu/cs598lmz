import lzma
# Test LZMADecompressor.seek() and LZMADecompressor.tell()

data = lzma.compress(b"hello world")

decompressor = lzma.LZMADecompressor()
decompressor.decompress(data[:2])
