import lzma
# Test LZMADecompressor

# Test that decompress() returns the empty bytes object when fed the empty bytes object
assert lzma.LZMADecompressor().decompress(b'') == b''

# Test that decompress() returns the empty bytes object when fed the empty bytearray object
assert lzma.LZMADecompressor().decompress(bytearray()) == b''

# Test that decompress() returns the empty bytes object when fed the empty memoryview object
assert lzma.LZMADecompressor().decompress(memoryview(b'')) == b''

# Test that decompress() returns the empty bytes object when fed the empty array object
assert lzma.LZMADecompressor().decompress(array.array('B', [])) == b''

# Test that decompress() returns the empty bytes object when fed the empty array object
assert lzma.LZMADecompressor().decompress(array.array('B', [0])) == b''

# Test that decompress() returns the empty bytes object when fed the empty array object

