import io
# Test io.RawIOBase
# (not in 2.7, part of 3.x)

# io.BufferedIOBase may appear in the future but we don't test it
# (requires some changes to the mmap module to support, that's the
#  only reason)

import unittest
