import codecs
# Test codecs.register_error

# This test is a bit of a hack, since it depends on the codecs module
# being able to decode the string 'abc'.  This is true for most codecs,
# but not all.

from test import test_support

class CodecsTestCase(unittest.TestCase):
    def test_register_error(self):
        # Test the register_error function
        import codecs
        import string
        def bad_decode(input, errors='strict'):
            raise UnicodeError, "bad decode"
        def bad_encode(input, errors='strict'):
            raise UnicodeError, "bad encode"
        def ignore_encode(input, errors='strict'):
            return (input, len(input))
        def ignore_decode(input, errors='strict'):
            return (u"\ufffd", len(input))
        def replace_encode(input, errors='strict'):
            return (u"?", len(input))
        def replace_decode(input, errors='strict'):
            return (u"
