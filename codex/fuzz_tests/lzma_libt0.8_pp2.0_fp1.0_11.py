import lzma
lzma_encode = None
lzma_decode = None
if hasattr(lzma, 'compress'):
    lzma_encode = lzma.compress
if hasattr(lzma, 'decompress'):
    lzma_decode = lzma.decompress
# PyPy
if lzma_encode is None or lzma_decode is None:
    import backports.lzma
    lzma_encode = backports.lzma.compress
    lzma_decode = backports.lzma.decompress


@check_key
def encode(s, key):
    """
    Encode a string.

    :param str s: String to encode.
    :param key: key.
    """
    data = lzma_encode(bz2_encode(s.encode()))
    data = aes_encode(data, key)
    return str(data)[2:-1]


@check_key
def decode(data, key):

