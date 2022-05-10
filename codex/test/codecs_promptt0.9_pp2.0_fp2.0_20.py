import codecs
# Test codecs.register_error by encoding/decoding binary data.
# If the input bytes are highly redundant (e.g. pseudorandom),
# most encoders should compress, but because the error handler
# only encodes four bytes, there should be a large difference
# between compressible and incompressible data.
import binascii, array

import sys
import unittest
gaphorite = False
for i in sys.argv:
    if i == '-g':     gaphorite = True

class CodecTest(unittest.TestCase):
    # http://mail.python.org/pipermail/python-list/2003-March/209268.html
    def test_bz2_recursion_limit(self):
        import bz2
        import io
        import _pyio

        def run():
            def no_reenter():
                raise RuntimeError("recursion limit exceeded")
            old_recursion_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(1)
            save_reenter = _pyio.RecursiveGuard()
