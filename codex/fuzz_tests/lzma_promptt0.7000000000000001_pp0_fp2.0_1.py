import lzma
# Test LZMADecompressor.decompress() with a string argument.

# This test case demonstrates a bug in the _lzma module from Python 2.7
# through Python 3.4.

# The bug causes _lzma.LZMADecompressor.decompress() to raise an exception
# when called with a string argument that contains an embedded null byte.

# The bug was fixed in Python 3.5.

# The bug is not present in the xz module.

# This test case is based on a test case submitted by Antoine Pitrou in issue
# #19933, and later enhanced by Serhiy Storchaka and Antoine Pitrou.

import contextlib
import io
from lzma import LZMADecompressor
from lzma import FORMAT_RAW, FILTER_LZMA2
from lzma.compat import compat_lzma_decompress
from test import support
from test.support import import_helper

try:
    import _lzma
except ImportError:
    raise unittest.SkipTest("_lzma module is not
