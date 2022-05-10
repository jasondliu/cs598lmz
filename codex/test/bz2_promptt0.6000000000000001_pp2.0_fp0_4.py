import bz2
# Test BZ2Decompressor with a single-byte read() call

# This test is based on test_bz2.BZ2Compressor.test_single_byte_read()
# from the Python 2.7.10 standard library test suite.

# The original test used a StringIO as the input source, which is not
# available in Python 3.
# Instead, we use a BytesIO.

from io import BytesIO
from bz2 import BZ2Decompressor
