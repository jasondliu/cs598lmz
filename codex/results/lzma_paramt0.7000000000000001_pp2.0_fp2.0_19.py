from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzma'

from . import lzma

from itertools import chain
from warnings import warnpy3k
from operator import itemgetter
from io import BytesIO

from .compat import (
    is_py2,
    is_py3,
    is_native_win,
    bytes_from_byte,
    is_bytes,
    is_unicode,
    to_bytes,
    to_unicode,
    to_string,
    to_unicode_each,
    is_zipfile,
    is_tarfile,
    is_7zfile,
    is_rarfile,
    is_lzmafile,
    is_bzip2file,
    is_gzipfile,
    is_arfile,
    is_xzfile,
    is_lzfile,
    is_tarfile_stream,
    is_zipfile_stream,
    is_7zfile_stream,
    is_rarfile_stream,
    is_lzmafile_stream,

