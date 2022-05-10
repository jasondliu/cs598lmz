import io
# Test io.RawIOBase.truncate

# This passes the reference implementation for io.StringIO and
# io.BytesIO, which close the stream when truncate is called, and so
# reset the current position to zero.  However, the Python 3.5
# documentation for io.RawIOBase.truncate does not specify closing the
# stream, and this would be a non-backward compatible change.

# The Python 3.5 documentation for io.FileIO says "This class should
# not be used directly, but is intended to be used by subclasses" and
# explicitly says that FileIO closes the file on truncate, which is
# the behavior I want to see here.

# The issue arises in issue #27575; a test case is attached.

class IOBaseTest(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b'0123456789')

    def test_truncate_no_args(self):
        self.f.seek(4)
        self.f.truncate()
        self.assertEqual(self
