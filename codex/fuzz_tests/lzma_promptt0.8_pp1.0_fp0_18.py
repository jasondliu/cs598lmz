import lzma
# Test LZMADecompressor
# Don't use the while loop and the try-except block
# in production code, it's just for demonstration
decompressor = lzma.LZMADecompressor()
compressed = open('compressed', 'rb').read()
uncompressed = decompressor.decompress(compressed)
print(uncompressed)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('hello.txt', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            with open('compressed', 'ab') as f:
                f.write(compressed)
        else:
            break
    remaining = compressor.flush()
    with open('compressed', 'ab') as f:
        f.write(remaining)

# Test LZMAFile
with lzma.open('hello.txt.xz', 'rt') as f:
    print(f.read())

with
