import lzma
lzma_comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
lzma_decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)

def compress_lzma(data):
    return lzma_comp.compress(data) + lzma_comp.flush()

def decompress_lzma(data):
    return lzma_decomp.decompress(data)

if lzma_decomp.decompress(lzma_comp.compress(b"test")) != b"test":
    print("LZMA compression/decompression test failed")
