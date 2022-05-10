from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: b''
LZMA_DECOMPRESSOR = LZMADecompressor()


def lzma_decompress(data, max_len=0, res=b''):
    """
    Decompress lzma data in chunks.

    This function is necessary because of lzma's way of handling decompression,
    which is to return None until all data is processed.

    This function is called recursively until all data is processed.

    Args:
        data (bytes): lzma compressed data.
        max_len (int): maximum size to decompress.
        res (bytes): decompressed data.

    Returns:
        bytes: decompressed data.
    """
    if len(data) == 0:
        return res
    elif max_len > 0 and len(res) >= max_len:
        return res
    else:
        decompressed = LZMA_DECOMPRESSOR.decompress(data)
        if decompressed is None:
            raise ValueError('Not enough data to decompress.')
        else:
           
