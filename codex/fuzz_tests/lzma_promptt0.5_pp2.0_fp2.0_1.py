import lzma
# Test LZMADecompressor
with lzma.open('data/enwik8.lzma') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read(100))
    print(data)

# Test LZMAFile
with lzma.open('data/enwik8.lzma') as f:
    data = f.read(100)
    print(data)

# Test LZMAStreamReader
with lzma.open('data/enwik8.lzma') as f:
    reader = lzma.LZMAStreamReader(f)
    data = reader.read(100)
    print(data)

# Test LZMAFile
with lzma.open('data/enwik8.lzma') as f:
    data = f.read(100)
    print(data)

# Test LZMAStreamReader
with lzma.open('data/enwik8.lzma') as f:
    reader = lzma.LZMAStreamReader
