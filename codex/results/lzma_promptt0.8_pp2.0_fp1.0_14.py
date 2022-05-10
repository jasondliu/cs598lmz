import lzma
# Test LZMADecompressor with fileno() and nframes() methods
import io
import sys
import time
import struct
import os
import tempfile
import traceback

# We rely on a few methods that were added in 3.2 and 3.3, so skip
# this test if the version is too old.
if sys.version_info[:2] < (3, 2):
    raise Exception('Test requires Python 3.2 or newer')

# For write_lzma_file()
import lzma

# Context manager to redirect sys.stdout.  Use it like this:
#
#   with captured_stdout() as stdout:
#       lzma.decompress(...)
#       ...
#   self.assertEqual(stdout.getvalue(), expected)
#
class captured_stdout(object):
    def __init__(self):
        self.stdout = sys.stdout
        sys.stdout = io.StringIO()

    def __enter__(self):
        return sys.stdout

    def __exit__(self, exc_type, exc_value,
