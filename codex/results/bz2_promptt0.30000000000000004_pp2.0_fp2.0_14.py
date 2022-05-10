import bz2
# Test BZ2Decompressor

with open('data/enwik9.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('data/enwik9', 'wb') as g:
        while True:
            block = f.read(1024)
            if not block:
                break
            g.write(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('data/enwik9.bz2', 'rb') as f:
    with open('data/enwik9', 'wb') as g:
        while True:
            block = f.read(1024)
            if not block:
                break
            g.write(block)

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik9.bz2', 'rb') as f:
    with open('data/enwik9', 'wb') as g:
        for block in iter(lambda: f.read(1024), b''):
            g
