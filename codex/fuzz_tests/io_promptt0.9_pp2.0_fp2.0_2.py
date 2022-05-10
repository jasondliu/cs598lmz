import io
# Test io.RawIOBase


class RawIOTest(unittest.TestCase):
    length = 10
    char = b'A'

    def test_read(self):
        with open(test.support.TESTFN, 'wb') as f:
            f.write(self.char * self.length)
        with open(test.support.TESTFN, 'rb', buffering=0) as fobj:
            self.assertNotIsInstance(fobj, io.BufferedReader)
            self.assertNotIsInstance(fobj, io.BufferedWriter)
            self.assertNotIsInstance(fobj, io.BufferedRandom)
            self.assertNotIsInstance(fobj, io.TextIOBase)
            self.assertIsInstance(fobj, io.RawIOBase)
            self.assertEqual(len(fobj.read(self.length)), self.length)
            self.assertEqual(len(fobj.read()), 0)

    def test_readall(self):
        with open(test.support.TESTFN, 'wb') as f:

