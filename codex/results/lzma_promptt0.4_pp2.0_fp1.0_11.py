import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
#decompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00')
decompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x16\x00\x00\x00')

# Test LZMACompressor
compressor = lzma.LZMACompressor()
data = b'This is the data to compress. It is not very long so the effect is not as visible.'
compressed = compressor.compress(data)
compressed += compressor.flush()

# Test LZMAFile
with lzma.open('/tmp/foo.xz', 'w') as f:
    f.write(b'hello world')

# Test LZMAError
try:
    raise lzma.LZMAError
except
