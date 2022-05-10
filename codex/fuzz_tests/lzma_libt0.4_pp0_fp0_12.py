import lzma
lzma.LZMA_PRESET = 9

def _get_lzma_decompressor():
    return lzma.LZMADecompressor()

def _get_lzma_compressor():
    return lzma.LZMACompressor(preset=9)

def _get_lzma_compress(data):
    return lzma.compress(data, preset=9)

def _get_lzma_decompress(data):
    return lzma.decompress(data)

def _get_lzma_open(mode, data):
    if mode == 'r':
        return lzma.LZMAFile(BytesIO(data))
    elif mode == 'w':
        return lzma.LZMAFile(BytesIO(), mode='w', preset=9)

def _get_lzma_file(mode, data):
    if mode == 'r':
        return lzma.LZMAFile(BytesIO(data))
    elif mode == 'w':
       
