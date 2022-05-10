import bz2
bz2.decompress(data)

# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = gzip.compress(s)
len(t)
gzip.decompress(t)

# bz2
import bz2
s = b'witch which has which witches wrist watch'
len(s)
t = bz2.compress(s)
len(t)
bz2.decompress(t)

# lzma
import lzma
s = b'witch which has which witches wrist watch'
len(s)
t = lzma.compress(s)
len(t)
lzma.decompress(t)

# zlib
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)

# filecmp
import filecmp
filecmp.cmp('/etc/passwd', '/etc/group')
file
