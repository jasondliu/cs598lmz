import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        chunk = decompressor.decompress(chunk)
        if chunk:
            print(chunk)

# Test BZ2File
with bz2.BZ2File(fn,'r',buffering=100000) as f:
    for line in f:
        print(line)

# Test BZ2File with a compression level
bz2.BZ2File(fn,'w',9)

import bz2

# test bz2.decompress, compress
s = 'hello world'
assert(s == bz2.decompress(bz2.compress(s)))

# test bz2.BZ2Decompressor.decompress
d = bz2.BZ2Decompressor()
assert(s == d.decompress(d.compress(s)))

# test bz2.BZ2File
with bz2.BZ2File
