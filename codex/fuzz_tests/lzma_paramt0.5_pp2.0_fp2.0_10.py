from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
compressed_data = bz2.compress(original_data)
bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = zlib.compress(original_data)
zlib.decompress(compressed_data)

# gzip
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'rb') as f:
    data = f.read()

with gzip.open('somefile.gz', 'wb') as f:
    f.write(data)

# brotli
import brotli
compressed_data = brotli.compress(original_data)
brotli.decompress(compressed_data)
