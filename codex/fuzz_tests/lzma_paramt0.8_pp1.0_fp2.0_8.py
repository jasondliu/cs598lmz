from lzma import LZMADecompressor
LZMADecompressor.supported_filters = [{'id': LZMA_FILTER_LZMA1}]

import sys
import io
import json

class NoMoreLinesException(Exception):
    """
    Thrown at the end of the file
    """
    pass

def _read_one_line(decomp: LZMADecompressor, recv_buffer: bytearray, max_line_length: int) -> bytes:
    """
    From a decompressor and a receiving buffer, this function
    will return one line, if enough data is available.

    It should be called again and again until a line is finally returned.

    If the receiving buffer is too short to store a whole line, it will be
    extended.

    If no line can be read because the file is finished, a NoMoreLinesException
    is raised.

    :param decomp:
        The LZMADecompressor which should be used.

    :param recv_buffer:
        The receiving buffer, probably containing leftovers. The length
        of this buffer will be the maximum line length.

    :
