import codecs
# Test codecs.register_error()

from test import test_support, unicode_helper
from test.test_support import TESTFN

class CodecOpenTest(unittest.TestCase):
    def setUp(self):
        self.fileobj = codecs.open(TESTFN, 'w', 'latin-1')
    def tearDown(self):
        self.fileobj.close()
        try:
            os.unlink(TESTFN)
        except os.error:
            pass
    def test_fileno(self):
        if hasattr(self.fileobj, 'fileno'):
            fd = self.fileobj.fileno()
            try:
                os.write(fd, "hello")
                self.fileobj.flush()
                self.assertEqual(os.stat(TESTFN).st_size, 5)
            except OSError as e:
                # From test_fileno.
                self.failUnlessEqual(e.errno, errno.EBADF)

    def test_incrementalencoder(self):
        e =
