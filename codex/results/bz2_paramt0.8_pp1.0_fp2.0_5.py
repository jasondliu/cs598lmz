from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor
from gzip import GzipFile
GzipFile = GzipFile
from . import lzma
from .lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor
import zlib
zlib = zlib


def open(filename, mode='r', compresslevel=9, encoding=None, errors=None,
         newline=None):
    """ Shorthand for the CompressedFile class
    """
    return CompressedFile(filename, mode, compresslevel, encoding, errors,
                          newline)


DEFAULT_BUFFER_SIZE = 8 * 1024


def _text_stream(filename, mode,
                 encoding=None, errors=None, newline=None):
    if 'b' in mode:
        bin_flag = True
    else:
        bin_flag = False

    for meth in [zlib.decompressobj, bz2.BZ2Decompressor, lzma.LZMADecompressor]:
        if meth is None:
            continue
       
