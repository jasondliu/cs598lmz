import lzma
# Test LZMADecompressor

# decompress a file
with open('data/xz/test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# decompress a stream
with open('data/xz/test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    for chunk in iter(lambda: f.read(1024), b''):
        data = decompressor.decompress(chunk)
        if data:
            print(data)

# decompress a stream with a context manager
with open('data/xz/test.xz', 'rb') as f:
    with lzma.LZMADecompressor() as decompressor:
        for chunk in iter(lambda: f.read(1024), b''):
            data = decompressor.decompress(chunk)
            if data:
                print(data)

# decompress a stream with a context manager
