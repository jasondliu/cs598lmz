import lzma
# Test LZMADecompressor.decompress with a non-LZMA stream.
# It should raise an exception.

cd = lzma.LZMADecompressor()
try:
    cd.decompress(b'1234')
except lzma.LZMAError:
    pass
else:
    print('Test failed')
# Test LZMADecompressor.decompress with a truncated stream.
# It should raise an exception.

cd = lzma.LZMADecompressor()
try:
    cd.decompress(b'\x00')
except lzma.LZMAError:
    pass
else:
    print('Test failed')
# Test LZMADecompressor.decompress with a truncated stream.
# It should raise an exception.

cd = lzma.LZMADecompressor()
try:
    cd.decompress(b'\xfd\xff\xff\xff\xff\xff\xff\xff')
except lzma.LZMAError:
    pass
