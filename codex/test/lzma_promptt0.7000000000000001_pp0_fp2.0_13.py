import lzma
# Test LZMADecompressor object for decompressing data incrementally.

from test import support
from test.support import run_unittest

from io import BytesIO
from lzma import LZMADecompressor
