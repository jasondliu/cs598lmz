from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor


def lzma_stream_decompressor():
    lz = LZMADecompressor()
    while True:
        block = yield
        output = lz.decompress(block)
        while output:
            yield output
            output = lz.unconsumed_tail



def xz_cmp(testfile, clevel):
    xz_compressor = LZMACompressor(clevel=clevel)
    xz_decompressor = LZMADecompressor()
    return bz2_cmp(testfile, xz_compressor, xz_decompressor)


def xz_strm_cmp(testfile, clevel):
    xz_compressor = LZMACompressor(clevel=clevel)
    xz_decompressor = lzma_stream_decompressor()
    next(xz_decompressor)
    return bz2_cmp(testfile, xz_compressor, xz_decompressor)


