import lzma
# Test LZMADecompressor

# This is the same test as test_lzma.py, but it uses the LZMADecompressor
# class instead of the lzma module functions.

import unittest
import os
from io import BytesIO
from test import support

from lzma import LZMADecompressor, FORMAT_RAW, CHECK_NONE
