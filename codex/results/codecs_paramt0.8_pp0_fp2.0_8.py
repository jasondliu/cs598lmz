import codecs
codecs.register_error('strict', codecs.ignore_errors)

class BZ2FileTestCase(unittest.TestCase):
    def setUp(self):
        self.bz2f = BZ2File(TESTFN, 'w')

    def tearDown(self):
        if self.bz2f:
            self.bz2f.close()
        os.unlink(TESTFN)

    def test_init(self):
        self.assertEqual(self.bz2f.name, TESTFN)
        self.assertEqual(self.bz2f.closed, 0)
        self.assertEqual(self.bz2f.mode, 'w')
        self.assert_(self.bz2f.myfileobj is None)

    def test_write(self):
        self.bz2f.write(b"foo")
        self.bz2f.close()
        self.assertEqual(
            bz2.decompress(open(TESTFN, 'rb').read()),
            b"foo"

