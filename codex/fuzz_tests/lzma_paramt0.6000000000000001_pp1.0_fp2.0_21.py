from lzma import LZMADecompressor
LZMADecompressor().decompress(LZMADecompressor().decompress(data))

# uncompress lzma
import lzma
with open('data.lz', 'rb') as f:
    data = f.read()
lzma.decompress(data)

# uncompress lzma
import lzma
with open('data.lz', 'rb') as f:
    data = f.read()
lzma.decompress(data, format=lzma.FORMAT_AUTO, memlimit=10485760)

# uncompress snappy
import snappy
snappy.uncompress(snappy.uncompress(data))

# uncompress snappy
import snappy
snappy.uncompress(snappy.uncompress(data))

# uncompress snappy
import snappy
snappy.uncompress(snappy.uncompress(data))

# uncompress snappy
import snappy
snappy.uncompress(snappy.uncompress(data))

# uncompress snappy
import snappy
