import lzma
# Test LZMADecompressor before we use it

# cdata = b"test"
# lzma_comp = lzma.LZMACompressor()
# cdata += lzma_comp.flush()
# print(type(cdata), cdata, len(cdata))
# lzma_decomp = lzma.LZMADecompressor()
# print(type(lzma_decomp.decompress(cdata)))
def wrap_encode(data, encoding="utf-8"):
    b = data.encode(encoding)
    lzma_comp = lzma.LZMACompressor()
    cdata = lzma_comp.compress(b)
    cdata += lzma_comp.flush()
    return base64.b64encode(cdata).decode("ascii")


def wrap_decode(data, encoding="utf-8"):
    cdata = base64.b64decode(data)
    lzma_decomp = lzma.LZMADecompressor()
    b =
