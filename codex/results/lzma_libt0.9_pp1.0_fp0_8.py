import lzma
lzma.__version__


#########################################################################
# Different compression formats and compression decoders
#########################################################################

def gunzip_open(path, mode='r'):
    """Opens a stream decompressing gzip-ed files on the fly.
    Mode 'w' is not supported.

    """
    if mode == 'r':
        return gzip.open(path, 'rb')
    else:
        raise NotImplementedError()

def bz2_open(path, mode='r'):
    """Opens a stream decompressing bz2-compressed files on the fly.
    Mode 'w' is not supported.

    """
    if mode == 'r':
        return bz2.BZ2File(path, 'rb')
    else:
        raise NotImplementedError()


def lzma_open(path, mode='r'):
    """Opens a stream decompressing lzma-ed files on the fly.
    Mode 'w' is not supported.

    """
    if mode == 'r':
        return lzma
