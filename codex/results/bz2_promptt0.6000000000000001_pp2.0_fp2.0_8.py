import bz2
# Test BZ2Decompressor
with open('data/enwik8', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/enwik8.tmp', 'wb') as g:
        for chunk in iter(lambda: f.read(100 * 1024), b''):
            g.write(decompressor.decompress(chunk))
        g.write(decompressor.flush())

# Test BZ2File
with bz2.open('data/enwik8.bz2', 'rt') as f:
    text = f.read()
print(len(text))

with bz2.open('data/enwik9.bz2', 'wt') as f:
    f.write(text)

with bz2.open('data/enwik9.bz2', 'rt') as f:
    text = f.read()
print(len(text))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
with open('data/enwik9', 'rb')
