import lzma
# Test LZMADecompressor and LZMACompressor
import socket
import struct
import sys
import unittest
import zlib

from test import support

TESTFN = support.TESTFN
TESTFN2 = TESTFN + "2"

# Create a test file for input
with open(TESTFN, "wb") as f:
    f.write(b"1234567890" * 10000)

class BaseTest:
    filename = TESTFN
    mode = "r"
    compress = 1
    compress_level = 6
    buffering = 1
    binary = 0
    errors = None
    encoding = None
    newline = None
    decoder = None
    read_size = 1024
    read_size_exception = None
    max_length = None
    max_length_exception = None
    max_buffer_size = None
    max_buffer_size_exception = None
    max_buffer_size_warning = None
    max_buffer_size_warning_limit = None
    init_function = None
    init_args = ()
    init_kwargs =
