from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2compressed)

# decompress a file input
with BZ2File(filename) as f, open(newfile, 'wb') as g:
    for block in iter(lambda: f.read(1024), b''):
        g.write(BZ2Decompressor().decompress(block))
