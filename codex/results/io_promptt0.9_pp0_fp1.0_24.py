import io
# Test io.RawIOBase

in_class = io.RawIOBase
out_class = io.RawIOBase
_buffer_size = 10

from test.test_io import BaseTestRawIO
from test.test_io import TestRawIOBase
class BaseTestRawBufferedIO(BaseTestRawIO):
    pass

class TestRawBufferedIOBase(_BaseRawBufferedIO,
                            TestRawIOBase,
                            BaseTestRawBufferedIO,
                            unittest.TestCase):
    pass

def test_main(verbose=None):
    supports_direct_io = True
    if verbose is None:
        verbose = 1
    tests = [TestRawBufferedIOBase]
    test_support.run_unittest(*tests)

if __name__ == '__main__':
    test_main(verbose=2)
