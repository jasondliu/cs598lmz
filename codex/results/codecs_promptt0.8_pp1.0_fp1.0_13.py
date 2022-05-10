import codecs
# Test codecs.register_error() with a fallback function that returns a
# string of length >1.

import test.test_support

def hex_escape(exception):
    return codecs.replace_errors(hex(ord(exception.object[exception.start]))[2:].zfill(2), exception.end)

class TestCodecs(unittest.TestCase):

    def test_defencoding(self):
        self.assert_(hasattr(sys, "getdefaultencoding"))
        enc = sys.getdefaultencoding()
        codecs.lookup(enc)  # Check that default encoding is legal

    def test_register(self):
        # default encoding detection
        import locale
        loc = locale.getpreferredencoding()
        self.assertEqual(codecs.lookup(loc).name, loc)
        if loc.lower().replace('_', '-').replace(' ', '-') == "us-ascii":
            self.assertEqual(codecs.lookup(loc).name, "ascii")
        def testfun(*
