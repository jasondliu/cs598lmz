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

class TestDecode(unittest.TestCase):
    def test_error_handling(self):
        # Test that the error handling callback is called when the
        # error is raised, and that it has the right arguments.
        #
        # This is a regression test for http://bugs.python.org/issue6704
        self.assertEqual(b'ab'.decode('ascii', 'add_one_codepoint'), u'a')
        self.assertEqual(b'ab'.decode('utf-16', 'add_one_codepoint'), u'a')
        self.assertEqual(b'abcd'.decode('utf-32', 'add_one_codepoint'), u'a')

        # This is a regression test for http://bugs.python.org/issue6705
        self.assertEqual(b'ab'.decode('ascii', 'add_utf16_bytes'), u'ab')
        self.assertEqual(b'ab'.decode('utf-16', 'add_utf16_bytes'), u'ab
