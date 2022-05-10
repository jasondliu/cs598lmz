import lzma
# Test LZMADecompressor
assert lzma.LZMADecompressor().decompress(b'') == b''
assert lzma.LZMADecompressor().decompress(b'test') == b'test'
assert lzma.LZMADecompressor().decompress(b'\x00\x00\x00\x00\x00') == b''
# Test LZMACompressor
assert lzma.LZMACompressor().compress(b'') == b''
assert lzma.LZMACompressor().compress(b'test') == b'test'
assert lzma.LZMACompressor().compress(b'\x00\x00\x00\x00\x00') == b'\x00\x00\x00\x00\x00'
# Test LZMAFile
assert lzma.LZMAFile(io.BytesIO(b''), 'r', None).read() == b''
assert lzma.LZMAFile(io.BytesIO(b'test'), 'r', None).
