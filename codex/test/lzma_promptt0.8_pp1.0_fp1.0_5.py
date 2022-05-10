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

