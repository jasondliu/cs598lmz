import bz2
# Test BZ2Decompressor
from bz2file import BZ2File
from bz2file import BZ2Compressor, BZ2Decompressor

import gzip
# Test GzipFile
from gzipfile import GzipFile
from gzipfile import GzipCompressor, GzipDecompressor

import lzma
# Test LZMADecompressor
from lzmafile import LZMAFile
from lzmafile import LZMACompressor, LZMADecompressor

import zlib
# Test Decompress
from zlibfile import ZlibFile
from zlibfile import ZlibCompressor, ZlibDecompressor

from io import BytesIO, BufferedReader

from test import support
from test import test_zipfile
from test.support import TESTFN, unlink, run_unittest

def _gen_test_data():
    yield b'abcdef' * 1024
    yield b'This is a test. ' * 1024
    yield b'\x00\x01\x02\x03\x04\x05\x06\x07
