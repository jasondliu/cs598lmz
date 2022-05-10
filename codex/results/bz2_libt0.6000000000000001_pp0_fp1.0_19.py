import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File(filename).read()

f = bz2.BZ2File('data/example4.bz2')
f.read()
f.close()

print('\n')

with bz2.BZ2File('data/example4.bz2') as f:
    print(f.read())

print('\n')

# use gzip
import gzip
with gzip.open('data/example6.gz', 'rt') as f:
    text = f.read()
    print(text)

# use zlib
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))

print('\n')

# use lzma
import lzma

with lzma.open('data/example
