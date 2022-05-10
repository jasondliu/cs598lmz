import lzma
# Test LZMADecompressor and LZMACompressor

def t_decomp(data):
    dc = lzma.LZMADecompressor()
    data = dc.decompress(data)
    if len(dc.unused_data) > 0:
        print("unused data", repr(dc.unused_data))
    print("len(data)", len(data))

