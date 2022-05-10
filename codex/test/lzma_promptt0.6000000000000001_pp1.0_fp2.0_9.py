import lzma
# Test LZMADecompressor(format=FORMAT_RAW, memlimit=None, filters=None)

data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
c = lzma.LZMADecompressor()
c.decompress(data)

