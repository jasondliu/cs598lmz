import lzma
# Test LZMADecompressor

def decompress(data, max_length=None):
    """Decompress LZMA-compressed data.

    If the data is compressed, the original uncompressed data is returned.
    If the data is not compressed, a ValueError is raised.

    The data can be either a bytes object or a file object.
    The data produced by this method can be larger than the original.
    If you want to limit the size of the output, set the optional argument
    max_length to the maximum length of data you want.
    """
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("can't decompress data; data should be bytes or "
                        "bytearray, not %s" % type(data).__name__)
    if len(data) < 5:
        raise ValueError("LZMA-compressed data too short")
    if data[0] != 0xFD or data[1:5] != b"7zXZ":
        raise ValueError("not an LZMA-compressed data")
    dec = LZMAD
