import lzma
# Test LZMADecompressor for bad input
#
# This test checks that LZMADecompressor raises an error when given
# incomplete input data.

import io

from test.support import run_unittest

