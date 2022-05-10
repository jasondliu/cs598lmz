import lzma
# Test LZMADecompressor

lzc = lzma.LZMADecompressor()

with open('data/xz/enwik8.xz', 'rb') as f:
    with lzma.open(f, 'rb') as xz_file:
        data = xz_file.read()
        print(data[:10])
        print(lzc.decompress(data[:10]))

# Test LZMACompressor

lzc = lzma.LZMACompressor()

with open('data/xz/enwik8.xz', 'rb') as f:
    with lzma.open(f, 'rb') as xz_file:
        data = xz_file.read()
        print(data[:10])
        print(lzc.compress(data[:10]))

# Test LZMADecompressor

lzc = lzma.LZMADecompressor()

with open('data/xz/enwik8.xz', 'rb') as f:
