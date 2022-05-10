import lzma
# Test LZMADecompressor on some data
try:
    # Test LZMADecompressor on some data
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    cd = lzma._decompressobj()
    dc = cd.decompress(data)
    assert dc == b''
except TypeError:
    # Test LZMADecompressor on some data
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    cd = lzma._decompressobj()
    dc = cd.decompress(data, max_length=0)
    assert dc == b''

try:
    # Test LZMADecompressor on some data
    data = b'\x00\x00\x00\x00\
