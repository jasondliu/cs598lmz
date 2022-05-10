import lzma
# Test LZMADecompressor.decompress()

# Decompress the entire stream.
decompressor = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    data = decompressor.decompress(f.read())
    print(data)

# Decompress a chunk at a time.
decompressor = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        data = decompressor.decompress(chunk)
        if data:
            print(data)

# Decompress the entire stream into a bytearray.
decompressor = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    data = decompressor.decompress(f.read(), max_length=10)
    print(data)
    data = decompressor.unused_data
    print(data)

#
