from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, unused: b""

def bzip2_decompress(data):
    decompressor = BZ2Decompressor()
    return decompressor.decompress(data)

def bz2_decompress(data):
    return bzip2_decompress(data)

def lzma_decompress(data):
    decompressor = LZMADecompressor()
    return decompressor.decompress(data)

def xz_decompress(data):
    return lzma_decompress(data)

def brotli_decompress(data):
    raise NotImplementedError()

def gzip_decompress(data):
    decompressor = GzipFile(fileobj=BytesIO(data))
    return decompressor.read()

def zlib_decompress(data):
    return zlib.decompress(data)

def deflate_decompress(data):
    return zlib.decompress(data, -zlib.MAX_WBITS)

def
