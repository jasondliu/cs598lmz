from lzma import LZMADecompressor
LZMADecompressor().decompress(frame_archive)

frame_archive # corrupt, needs to be fixed

# Fixing a Frame Archive
from lzma import LZMAError
LZMADecompressor().decompress(frame_archive) # raises LZMAError

frame_archive += b"\x00" * 16

LZMADecompressor().decompress(frame_archive) # now works

## Writing a Frame Archive
from typing import List
from tempfile import TemporaryFile

from lzma.compress import LZMACompressor
from lzma.checksum import crc32

from lzw import lzw_encode, lzw_decode

# lzw_encode and lzw_decode written for Chapter 11

def compress(uncompressed: bytes, wbits: int, dict_size: int) -> bytes:
    """
    Compress a block of data with LZW
    """
    dictionary = {bytes((i,)): i for i in range(dict_size)}
    output = []
    dict_size
