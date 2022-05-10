import lzma
# Test LZMADecompressor's ability to decompress data in chunks.
# This tests the internal state handling.

decomp = lzma.LZMADecompressor()

# If there is no input available, LZMADecompressor.decompress() will return
# empty bytes.
assert decomp.decompress(b'') == b''

# Decompress a single byte at a time, in the middle of the compressed data.
#
# The first chunk is short because it triggers the "initialize dictionary"
# state, which requires a larger chunk to initialize.
data = open('lzma_data.xz', 'rb').read()
for i in range(0x20, len(data), 0x80):
    decomp = lzma.LZMADecompressor()
    assert decomp.decompress(data[:i]) == b''
    assert decomp.decompress(data[i:i+1]) == b''
    assert decomp.decompress(data[i+1:]) == expected

# Decompress one byte at a time.
data = open('lz
