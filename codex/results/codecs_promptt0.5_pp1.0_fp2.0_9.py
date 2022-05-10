import codecs
# Test codecs.register_error

import codecs
import unittest

class TestCodecs(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error

        # Test registration of a function
        def my_ignore_error(message):
            return (u'', len(message))
        codecs.register_error('my_ignore', my_ignore_error)
        self.assertEqual(codecs.lookup_error('my_ignore'),
                         my_ignore_error)

        # Test registration of a name
        codecs.register_error('my_replace', 'replace')
        self.assertEqual(codecs.lookup_error('my_replace'),
                         codecs.lookup_error('replace'))

        # Test registration of an instance
        class MyIgnoreError(Exception):
            def __init__(self, message, startpos, endpos):
                self.message = message
                self.startpos = startpos
                self.endpos = endpos
            def __str__(self):
                return self
