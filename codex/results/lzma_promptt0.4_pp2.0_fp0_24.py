import lzma
# Test LZMADecompressor with a file-like object

data = b"x" * 100000 + lzma.compress(b"foo") + b"x" * 100000

with open("foo.xz", "wb") as f:
    f.write(data)

with open("foo.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    with decompressor.stream(f) as d:
        print(d.read())

# Test LZMADecompressor with a callback function

def read_and_decompress(compressed_data):
    decompressor = lzma.LZMADecompressor()
    return decompressor.decompress(compressed_data)

with open("foo.xz", "rb") as f:
    print(read_and_decompress(f.read()))
