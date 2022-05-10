import lzma
# Test LZMADecompressor

with lzma.open('data/enwik8.xz') as f:
    decomp = lzma.LZMADecompressor()
    print(decomp.decompress(f.read()))

# Test LZMADecompressor.read()

with lzma.open('data/enwik8.xz') as f:
    decomp = lzma.LZMADecompressor()
    print(decomp.read(f.read()))

# Test LZMADecompressor.read1()

with lzma.open('data/enwik8.xz') as f:
    decomp = lzma.LZMADecompressor()
    print(decomp.read1(f.read()))

# Test LZMADecompressor.multi_decompress()

with lzma.open('data/enwik8.xz') as f:
    decomp = lzma.LZMADecompressor()
    print(decomp.multi_decompress(f.read
