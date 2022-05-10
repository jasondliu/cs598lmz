import lzma
lzma.decompress(lzma_data)

# bzip2
import bz2
bz2_data = bz2.compress(b'witch which has which witches wrist watch')
bz2.decompress(bz2_data)

# gzip
import gzip
s = b'witch which has which witches wrist watch'
gzip_data = gzip.compress(s)
gzip.decompress(gzip_data)

# zlib
import zlib
s = b'witch which has which witches wrist watch'
zlib_data = zlib.compress(s)
zlib.decompress(zlib_data)
