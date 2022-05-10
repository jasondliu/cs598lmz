import lzma
# Test LZMADecompressor with no data
lzc = lzma.LZMADecompressor()
try:
    lzc.decompress(b'')
except EOFError:
    pass
else:
    print("Did not raise EOFError when no data given")
# Test LZMADecompressor with short data
lzc = lzma.LZMADecompressor()
try:
    lzc.decompress(b'\x00'*16)
except ValueError:
    pass
else:
    print("Did not raise ValueError when short data given")
# Test LZMADecompressor with data that's not an LZMA stream
lzc = lzma.LZMADecompressor()
try:
    lzc.decompress(b'\x00'*5)
except ValueError:
    pass
else:
    print("Did not raise ValueError when no data given")
# Test LZMADecompressor with truncated stream
lzc = lzma.LZMADecompressor()

