import lzma
# Test LZMADecompressor constructor
try:
    lzma.LZMADecompressor()
except RuntimeError:
    # lzma module segfaults
    import unittest
    raise unittest.SkipTest("lzma module segfaults")

import bz2
