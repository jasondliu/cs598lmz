import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_run(testfunc):
    with test.support.check_warnings(quiet=True):
        test.support.run_unittest(testfunc)

#==========================================================================

class IOTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform == 'win32',
                         'test specific to Windows Unicode filesystem')
    def test_mbcs_file(self):
        # Issue #8136: Check that mbcs encoding can write a file with
        # a non-ascii name.
        nonascii = b'\xff'
        filename = nonascii.decode('mbcs')
        tmpdir = os.path.dirname(__file__) or os.curdir
        tmpdir = os.path.join(tmpdir, "io-test-%s" % filename)
        self.addCleanup(test.support.rmtree, tmpdir)
        # On Windows, the file is created with the short (8.3) name,
        # and the long name is available only after
