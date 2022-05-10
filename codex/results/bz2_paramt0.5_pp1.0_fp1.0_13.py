from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"hello world"))

# zlib
import zlib

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# lzma
import lzma

lzma.compress(s)
lzma.decompress(t)

# gzip
import gzip

gzip.compress(s)
gzip.decompress(t)

# zipfile
import zipfile

f = open('/tmp/example.zip', 'wb')
zf = zipfile.ZipFile(f)
zf.write('README.md')
zf.close()
f.close()

zf = zipfile.ZipFile('/tmp/example.zip')
zf.extractall()
zf.close()

zf = zipfile.ZipFile('/tmp/example.zip')

