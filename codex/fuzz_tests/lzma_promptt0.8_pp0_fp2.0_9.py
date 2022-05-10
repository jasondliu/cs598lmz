import lzma
# Test LZMADecompressor
try:
    lzma.LZMADecompressor()
    lzma_mode = lzma.FORMAT_XZ
except AttributeError:
    lzma_mode = lzma.FORMAT_ALONE
def gunzip_byte_data(data, mode=zlib.MAX_WBITS|16):
    with io.BytesIO(bytes(data)) as gz_file:
        with gzip.GzipFile(fileobj=gz_file, mode='rb') as decompressed:
            return decompressed.read()


def unxz_byte_data(data):
    with io.BytesIO(bytes(data)) as xz_file:
        decompressor = lzma.LZMADecompressor(format=lzma_mode)
        decompressed = decompressor.decompress(xz_file.read())
        return decompressed


def lzma_byte_data(data):
    with io.BytesIO(bytes(data)) as lzma_file:
        decompressor = lzma.LZM
