from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.BZ2Decompressor.decompress(data)
# bz2.decompress(data)

# zlib.decompress(data)
# zlib.decompress(data, wbits=zlib.MAX_WBITS|16)
# zlib.decompress(data, wbits=15|16)

# lzma.decompress(data)
# lzma.decompress(data, format=lzma.FORMAT_ALONE)

# lzma.LZMADecompressor().decompress(data)
# lzma.LZMADecompressor(format=lzma.FORMAT_ALONE).decompress(data)

# gzip.decompress(data)
# gzip.decompress(data, wbits=zlib.MAX_WBITS|16)

# gzip.GzipFile(fileobj=io.BytesIO(data)).read()
# gzip.GzipFile(fileobj=io
