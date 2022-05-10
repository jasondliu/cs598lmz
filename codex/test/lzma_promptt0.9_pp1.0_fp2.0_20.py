import lzma
# Test LZMADecompressor with valid data,
# and invalid data

# TODO: move this to test_lib_compress?

# note: the first test with valid data is also in test_lzma.py

import shutil
import sys
import types
import io

from test import support

