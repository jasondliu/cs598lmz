import _struct
# Test _struct.Struct.
import _testcapi

@contextlib.contextmanager
def use_large_memory_pages():
    """
    Return a context manager which sets and resets the _testcapi
    'test_large_memory_pages' flag.

    The test_large_memory_pages flag enables various workarounds in the
    interpreter for large memory pages.

    """
    try:
        if sys.version_info[:2] > (3, 5):
            was = _testcapi.get_large_memory_pages()
            _testcapi.set_large_memory_pages(True)
            yield
        else:
            yield
    finally:
        if sys.version_info[:2] > (3, 5):
            _testcapi.set_large_memory_pages(was)

class FormatStringTests(unittest.TestCase):
    def test_format_string(self):
        self.assertEqual('%#08x' % 10, _struct.calcsize('=I') < 4 and '0xa' or '0x0000000a
