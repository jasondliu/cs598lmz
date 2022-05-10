import lzma
# Test LZMADecompressor

with open('../data/compressed.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor(lzma.FORMAT_AUTO, None)
    data = f.read()
    res = decompressor.decompress(data)
    print(res[:100])

# Close
decompressor.flush()

# Test LZMAFile
with lzma.open('../data/compressed.xz', 'rt') as f:
    res = f.read()
    print(res[:100])

# Test Streaming with read
with lzma.open('../data/compressed.xz', 'rt') as f:
    res = f.read(1000)
    print(res[:300])

# Test Streaming with iter
with lzma.open('../data/compressed.xz', 'rt') as f:
    res = ''.join(f)
    print(res[:100])

# Test bz2 Module

# Test bz2file
import bz
