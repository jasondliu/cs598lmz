fn = lambda: None
# Test fn.__code__ checksum.
test_fn.__code__.co_code = b'foo'

fp = io.BytesIO()


@contextlib.contextmanager
def patch_code_checksum(_patch, _original):
    original_code_checksum = code.code_checksum
    code.code_checksum = _patch
    try:
        yield
    finally:
        code.code_checksum = _original


class TestJavaSerializer(unittest.TestCase):

    def setUp(self):
        self.serializer = serializer.JavaSerializer(fp)

    def test_write_stop(self):
        self.serializer.write_stop()
        self.assertEqual(fp.getvalue(), b'\x00')

    def test_write_long_string(self):
        self.serializer.write_long_string(b'\x00\x00')
        self.assertEqual(fp.getvalue(), b'\x01\x00\x00\x00\x00\x00')

    def test_write_
