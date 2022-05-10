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

class CodecTest(unittest.TestCase):

    # This is the list of test files.
    # Files must be named [testname].txt.
    # The first line of each file is the test name.
    # The second line is the encoding name
    # The third line is the error mode
    # The rest is the input data.
    testfiles = []

    def setUp(self):
        self.testfiles = []
        # Modules to remove from sys.modules during the test.
        self.to_remove = []

    def tearDown(self):
        import sys
        # Remove modules added during the tests.
        for modname in self.to_remove:
            if modname in sys.modules:
                del sys.modules[modname]

    def add_test(self, t):
        self.testfiles.append(t)

    # This is the list of all encodings from the Unicode database.
    # It includes the encodings from aliases and from mbcs.encodings,
    # minus those from the aliases and from the mbcs
