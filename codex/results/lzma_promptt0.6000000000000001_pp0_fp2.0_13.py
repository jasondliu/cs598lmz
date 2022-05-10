import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
with open('data/enwik9', 'rb') as f:
    data = f.read()
print(decomp.decompress(data))

# Test LZMACompressor
comp = lzma.LZMACompressor()
with open('data/enwik9', 'rb') as f:
    data = f.read()
print(comp.compress(data))

comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
with open('data/enwik9', 'rb') as f:
    data = f.read()
print(comp.compress(data))

comp = lzma.LZMACompressor(format=lzma.FORMAT_XZ)
with open('data/enwik9', 'rb') as f:
    data = f.read()
print(comp.compress(data))

comp = lzma.LZMACompressor(format=lzma.FORMAT_RAW)
with open
