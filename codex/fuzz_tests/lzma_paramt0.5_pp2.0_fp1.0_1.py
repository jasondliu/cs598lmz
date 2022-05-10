from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\xff\xff')

# Issue #26218: LZMADecompressor.decompress() should accept bytearray
with BytesIO(b'\x5d\x00\x00\xff\xff') as f:
    LZMADecompressor().decompress(bytearray(f.read()))

# Issue #26218: LZMADecompressor.decompress() should accept memoryview
with BytesIO(b'\x5d\x00\x00\xff\xff') as f:
    LZMADecompressor().decompress(memoryview(f.read()))

# Issue #26218: LZMADecompressor.decompress() should accept array.array
with BytesIO(b'\x5d\x00\x00\xff\xff') as f:
    LZMADecompressor().decompress(array.array('B', f.read()))

# Issue #26218: LZ
