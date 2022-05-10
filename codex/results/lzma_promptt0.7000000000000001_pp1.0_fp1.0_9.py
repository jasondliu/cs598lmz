import lzma
# Test LZMADecompressor.flush()

# Test with data read from a file
with lzma.open("../data/lorem_ipsum.txt.xz") as f:
    decomp = lzma.LZMADecompressor()
    data = f.read(10)
    buf = decomp.decompress(data)
    print(repr(buf))
    buf = decomp.flush()
    print(repr(buf))

# Test with data read from a byte string
with lzma.open("../data/lorem_ipsum.txt.xz") as f:
    decomp = lzma.LZMADecompressor()
    data = f.read(10)
    buf = decomp.decompress(data)
    print(repr(buf))
    buf = decomp.flush()
    print(repr(buf))

# Test with data read from a memory buffer
with open("../data/lorem_ipsum.txt.xz", "rb") as f:
    decomp = lzma.LZMADecompressor()
    data
