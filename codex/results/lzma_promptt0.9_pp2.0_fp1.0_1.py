import lzma
# Test LZMADecompressor.__init__(), and LZMADecompressor.__call__()

# Create an LZMA object to decompress data incrementally.
d = lzma.LZMADecompressor()

# Feed data in chunks, and collect the results.
data = []
with open('readme.txt.xz', 'rb') as f:
    for block in iter(lambda: f.read(32 * 1024), b''):
        data.append(d.decompress(block))

# All data fed, flush the last block.
d.flush()

print(len(b''.join(data)))
