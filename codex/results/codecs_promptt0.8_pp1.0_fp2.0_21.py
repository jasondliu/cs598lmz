import codecs
# Test codecs.register_error() (SPI)
import _testcapi
AUTO = _testcapi.AUTO

# line-endings are stripped automatically
# encoding is configurable here
TEST_LINES = [
    'a\n',
    'b\n',
    'c\n'
]

# codecs.register_error() tests

class R(object):
    """Recursive codec error handler."""
    def __init__(self, testcase):
        self.testcase = testcase
        self.counter = {}

    def __call__(self, encoding, exc):
        for key in ('name', 'reason', 'encoding', 'start', 'end'):
            self.testcase.assertTrue(hasattr(exc, key))
            value = getattr(exc, key)
            self.testcase.assertTrue(type(value) is str)
        self.testcase.assertTrue(hasattr(exc, 'object'))
        obj = getattr(exc, 'object')
        self.testcase.assertTrue(type(obj) is bytes)

