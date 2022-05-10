import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()
data = b'input data goes here'
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test LZMAFile
with lzma.open('data.xz', 'wb') as f:
    f.write(b'Foo bar baz')
with lzma.open('data.xz', 'rb') as f:
    data = f.read()
print(data)

# Test LZMAError
try:
    decompressor.decompress(b'nonsense')
except lzma.LZMAError as e:
    print(e)

# Test LZMAStreamReader
with open('data.xz', 'rb') as f:
    with lzma.LZMAStreamReader(f) as strm:
        for line in strm:
            print(repr
