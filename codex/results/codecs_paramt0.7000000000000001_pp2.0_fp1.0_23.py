import codecs
codecs.register_error('my', lambda x: (u'X', x.start + 1))
codecs.register_error('my2', lambda x: (x.group(0), x.start + 1))

#my1 = lambda x: (u'X', x.start + 1)
#my2 = lambda x: (x.group(0), x.start + 1)

class CodecsTestCase(unittest.TestCase):

    def test_bug_4489(self):
        # Issue 4489: ensure that the surrogatepass error handler does
        # not skip over undecodable bytes.
        self.assertEqual(b"abc\xff\u0100".decode("ascii", "surrogatepass"),
                         "\ufffd\ufffd\ufffd\ufffd\ufffd")

    def test_bug_3463(self):
        # Issue 3463: check that the ignore error handler skips over
        # undecodable bytes.
        self.assertEqual(b"abc\xff\u0100".decode("ascii", "ignore"), "abc")


