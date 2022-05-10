import codecs
# Test codecs.register_error() is correct.

import test.support, unittest

class TestCodecs(unittest.TestCase):

    def test_register_error(self):
        # Test raise an exception
        # Test a callable
        import codecs
        self.assertRaises(TypeError,
                          codecs.register_error, 'strictxxx')
        import string
        codecs.register_error('stringescape',
                              codecs.lookup_error('stringescape'))

    def test_codecs_lookup_error(self):
        # Test codecs.lookup_error
        import codecs
        self.assertRaises(LookupError, codecs.lookup_error, 'xxx')

        tmp = codecs.lookup_error('strict')
        codecs.lookup_error('strict')

        codecs.lookup_error('replace')

        codecs.lookup_error('ignore')

        codecs.lookup_error('backslashreplace')

        codecs.lookup_error('xmlcharrefreplace')



