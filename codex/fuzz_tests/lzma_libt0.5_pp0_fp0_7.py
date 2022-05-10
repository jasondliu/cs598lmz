import lzma
lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=[{"id": lzma.FILTER_DELTA, "dist": 1}])

def lzma_delta_compress(data):
    return lzma.compress(data, format=lzma.FORMAT_RAW, filters=[{"id": lzma.FILTER_DELTA, "dist": 1}])

def lzma_delta_decompress(data):
    return lzma.decompress(data, format=lzma.FORMAT_RAW)

def lzma_delta_decompress_safe(data):
    try:
        return lzma.decompress(data, format=lzma.FORMAT_RAW)
    except:
        return None

def lzma_delta_decompress_safe_with_padding(data, padding=8):
    try:
        return lzma.decompress(data, format=lzma.FORMAT_RAW)
    except:
       
