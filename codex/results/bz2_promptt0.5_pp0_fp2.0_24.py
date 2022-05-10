import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
with open('data/enwik8.bz2', 'rb') as f:
    d.decompress(f.read(1000))
# Test BZ2File
with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    data = f.read(1000)
data

# Test LZMACompressor
l = lzma.LZMACompressor()
with open('data/enwik8.bz2', 'rb') as f:
    l.compress(f.read(1000))
# Test LZMAFile
with lzma.LZMAFile('data/enwik8.bz2', 'rb') as f:
    data = f.read(1000)
data

# Test LZMADecompressor
l = lzma.LZMADecompressor()
with open('data/enwik8.bz2', 'rb') as f:
    l.decompress(f.read(1000))

