from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# bz2.BZ2File
# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)

t = gzip.compress(s)
len(t)

gzip.decompress(t)

# gzip.GzipFile
# gzip.compress()
# gzip.decompress()

# lzma
import lzma
s = b'witch which has which witches wrist watch'
len(s)

t = lzma.compress(s)
len(t)

lzma.decompress(t)

# lzma.
