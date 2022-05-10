import lzma
# Test LZMADecompressor.
#
# This module defines two functions: a "decompress" function that decodes
# the input data into a Python unicode object, and a "StreamReader" class
# that can be used to read LZMA-compressed data incrementally.
#
# Usage:
#
#     import lzma
#
#     print(lzma.decompress(b"Hello world!"))
#
#     stream = lzma.StreamReader(
#         lzma.input_stream(input_file),
#         lzma.decompress)
#     data = stream.read()

from io import RawIOBase

from . import _lzma


def input_stream(input_file):
    """
    Return a new file object that reads the compressed data from the given
    file object.
    """
    return _lzma.open(input_file, mode="rb")


def _read_compressed_size(input_file):
    header = input_file.read(12)
    magic = header[0:6]
    if magic
