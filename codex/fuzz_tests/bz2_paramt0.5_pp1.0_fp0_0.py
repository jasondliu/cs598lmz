from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 2. zlib
# zlib.decompress(data, wbits=MAX_WBITS)
# wbits = 15 + 32 (gzip)
# wbits = -15 (zlib)

# 3. gzip
import gzip
gzip.decompress(data)

# 4. lzma
# lzma.LZMADecompressor().decompress(data)

# 5. lz4
# lz4.block.decompress(data)

# 6. lz4framed
# lz4f.decompress(data)

# 7. lzma_stream
# lzma_stream.decompress(data)

# 8. lzo
# lzo.decompress(data)

# 9. lzw
# lzw.decompress(data)

# 10. lzf
# lzf.decompress(data)

# 11. lzma_alone
# lzma_alone.decompress(data
