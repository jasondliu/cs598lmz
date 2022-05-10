import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()

data = d.decompress(compressed_data)

print(data)

# Test LZMADecompressor.decompress()
d = lzma.LZMADecompressor()

with open('file.txt.xz', 'rb') as f:
    for chunk in iter(lambda: f.read(32 * 1024), b''):
        d.decompress(chunk)

print(d.unused_data)

# Test LZMADecompressor.flush()
d = lzma.LZMADecompressor()

with open('file.txt.xz', 'rb') as f:
    for chunk in iter(lambda: f.read(32 * 1024), b''):
        data = d.decompress(chunk)
        if data:
            print(data)

print(d.flush())

# Test LZMADecompressor.decompress() with a bad stream
d = lzma.LZM
