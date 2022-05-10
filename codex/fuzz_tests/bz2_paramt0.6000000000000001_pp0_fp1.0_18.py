from bz2 import BZ2Decompressor
BZ2Decompressor.decompress(bz2_compress(data))

# <codecell>

def bz2_decompress(data):
    decompressor = BZ2Decompressor()
    return decompressor.decompress(data)

# <codecell>

bz2_decompress(bz2_compress(data))

# <codecell>

import zlib
zlib.decompress(zlib.compress(data))

# <codecell>

def zlib_compress(data):
    compressor = zlib.compressobj(1)
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    return compressed

# <codecell>

zlib_compress(data)

# <codecell>

import gzip
gzip.decompress(gzip.compress(data))

# <codecell>

def gzip_compress(data):
    buf = BytesIO()
    with gzip.GzipFile(fileobj=buf, mode='wb')
