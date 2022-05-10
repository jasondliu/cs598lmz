import io
# Test io.RawIOBase


class RawIOTest(unittest.TestCase):

    @unittest.skipUnless(support.FS_NONASCII,
        'need support.FS_NONASCII for mktemp()')
    @unittest.skipUnless(hasattr(io, 'RawIOBase'),
        'test needs io.RawIOBase')
    def test_encoding(self):
        fname = support.TESTFN_UNICODE
        try:
            fd = open(fname, 'wb')
        except UnicodeEncodeError:
            self.skipTest('need non-ascii filesystem encoding')
        f = io.FileIO(fd.fileno(), 'r', encoding='utf-8')
        try:
            self.assertEqual(f.name, fname)
        finally:
            fd.close()
            f.close()
            support.unlink(fname)


class OtherRawTests(unittest.TestCase):

    def test_closed_is_true(self):
        raw = io.RawIOBase()

