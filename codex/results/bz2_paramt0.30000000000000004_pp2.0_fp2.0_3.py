from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
# bz2.decompress()

# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)

t = gzip.compress(s)
len(t)

gzip.decompress(t)

f = gzip.open('file.gz', 'wt')
f.write('"Hello, world!"')
f.close()

gzip.open('file.gz', 'rt').read()

# gzip.compress()
# gzip.decompress()
# gzip.open()

# lzma
import lzma
s = b'witch which has which witches wrist watch'
len(s)

t = lzma.compress(s)
len(t)

lzma.decompress(t)

f = lzma.open('file.xz', 'wt')
f.write('"Hello, world!"')
f.close()

lzma
