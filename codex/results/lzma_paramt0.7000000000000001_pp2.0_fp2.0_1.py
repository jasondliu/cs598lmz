from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: self.decompress(b"", True)

def lzma_decompress(data: bytes, size: int) -> bytes:
    """
    Decompress lzma compressed data.

    Parameters
    ----------
    data : bytes
        lzma compressed data
    size : int
        uncompressed size
    """
    decompressor = LZMADecompressor()
    return decompressor.decompress(data, size)


def lz4_decompress(data: bytes, size: int) -> bytes:
    """
    Decompress LZ4 compressed data.

    Parameters
    ----------
    data : bytes
        LZ4 compressed data
    size : int
        uncompressed size
    """
    return lz4.block.decompress(data, size)


def compress(data: bytes, compression: str) -> bytes:
    """
    Compress with the given compression.

    Parameters
    ----------
    data : bytes
        data which should be compressed
    compression : str
        method of compression
   
