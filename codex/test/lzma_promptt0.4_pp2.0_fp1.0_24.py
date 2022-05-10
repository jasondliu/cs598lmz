import lzma
# Test LZMADecompressor

d = lzma.LZMADecompressor()

# Decompress a file
with open('test.xz', 'rb') as f:
    decompressed_data = d.decompress(f.read())

# Decompress a stream
with open('test.xz', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
