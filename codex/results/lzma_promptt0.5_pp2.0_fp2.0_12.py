import lzma
# Test LZMADecompressor

lzc = lzma.LZMADecompressor()

with open('../data/enwik8', 'rb') as f:
    data = f.read(100)
    while data:
        decompressed = lzc.decompress(data)
        if decompressed:
            print(decompressed)
            break
        data = f.read(100)

# Test LZMACompressor

lzc = lzma.LZMACompressor()

with open('../data/enwik8', 'rb') as f:
    data = f.read(100)
    while data:
        compressed = lzc.compress(data)
        if compressed:
            print(compressed)
            break
        data = f.read(100)

# Test LZMAFile

with lzma.open('../data/enwik8') as f:
    for line in f:
        print(line)
        break

# Test LZMAFile

with lzma.open('../data/enwik8')
