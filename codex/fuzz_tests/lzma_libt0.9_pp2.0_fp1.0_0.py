import lzma
lzma = lzma


def decompress_lzma(data):
    ret, _ = lzma.decompress(data)
    return ret


lzma_decompress = decompress_lzma
