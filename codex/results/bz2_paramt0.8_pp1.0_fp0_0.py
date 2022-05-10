from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = "bz2"

__version__ = "0.3"


def uncompress(data, max_length=0):
    """Decompresses bzip2 compressed data.

    data: The string containing compressed data.
    max_length: The maximum length allowed for the decompressed string.
        The default, 0, means no limit.
    Raises ValueError if the compressed data is corrupted, or there is more
    than max_length bytes of uncompressed data.
    """

    if len(data) < 4:
        raise ValueError("Compressed data too short")
    magic = data[0:3]
    if magic != 'BZh':
        raise ValueError("Invalid bzip2 data")
    block_size = ord(data[3]) - 48
    if block_size < 1 or block_size > 9:
        raise ValueError("Invalid bzip2 block size")

    # Set up bitstream reader
    data = data[4:]
    if data[-2:] != '\x00\x00':
        raise ValueError("Invalid bzip2 data
