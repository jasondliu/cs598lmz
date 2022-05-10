import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMACompressor
with open('test.xz', 'wb') as f:
    compressor = lzma.LZMACompressor()
    data = compressor.compress(b'Hello World!')
    data += compressor.flush()
    f.write(data)

# Test LZMAFile
with lzma.open('test.xz', 'w') as f:
    f.write(b'Hello World!')

with lzma.open('test.xz', 'r') as f:
    print(f.read())

# Test LZMAError
try:
    lzma.decompress(b'\x00')
except lzma.LZMAError as e:
    print(e)

# Test is_check_supported
print(lzma.is_check_supported
