import lzma
lzma_algo = lzma.LZMADecompressor()

def do_decompress(blob):
    return lzma_algo.decompress(blob)

def do_compress(blob):
    return lzma_algo.compress(blob)
