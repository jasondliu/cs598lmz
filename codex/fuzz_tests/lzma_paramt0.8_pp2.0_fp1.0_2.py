from lzma import LZMADecompressor
LZMADecompressor.create_compress_filter()


# --- functions ---

def get_lzma_block_info(data):
    info = data[:13]
    if len(info) != 13:
        raise EOFError

    props, dsz, usz = (
        info[0],  # lc, lp and pb in normal order
        info[1:5], # dsz
        info[5:9]  # usz
    )
    dsz = int.from_bytes(dsz, 'little')
    usz = int.from_bytes(usz, 'little')

    return props, dsz, usz

def _decompress_lzma(data):
    return LZMADecompressor().decompress(data)

def decompress_lzma(data, dsz, usz):
    """Decompress a single lzma compressed block
    data is the compressed data
    dsz is the size of compressed data in bytes
    usz is the size of decompressed data in bytes
   
