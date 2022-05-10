import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
data = b'This is the original text.'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls

decompressor = lzma.LZMADecompressor()
decompressed = b''
while True:
    buf = decompressor.decompress(compressed)
    if buf == b'':
        break
    decompressed += buf

print(decompressed)
# Test LZMADecompressor.unused_data

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

try:
    decompressor.decompress(b'This is more data.')
except lzma.LZMAError as e:
    print(e
