import lzma
# Test LZMADecompressor
with open('../data/ubuntu-12.04.5-server-amd64.iso', 'rb') as f:
    data = f.read()
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test LZMACompressor
with open('../data/ubuntu-12.04.5-server-amd64.iso', 'rb') as f:
    data = f.read()
comp = lzma.LZMACompressor()
comp.compress(data)
comp.flush()

# Test compress
lzma.compress(b'Hello')

# Test decompress
lzma.decompress(b'Hello')

# Test open
lzma.open('../data/ubuntu-12.04.5-server-amd64.iso', mode='rb')
lzma.open('../data/ubuntu-12.04.5-server-amd64.iso', mode='rb', format=lzma.FORMAT_ALONE)
lzma.open('../data/ubuntu-
