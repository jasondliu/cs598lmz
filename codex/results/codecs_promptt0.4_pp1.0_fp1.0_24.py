import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def strict_decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, {ord(c): c for c in 'abc'})

def strict_encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, {ord(c): c for c in 'abc'})

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler
        codecs.register_error('strict', raise_exc)
        self.assertEqual(strict_decode(b'\xff'), ('\ufffd', 1))
        self.assertEqual(strict_encode('\u1234'), (b'\xfd', 1))

        codecs.register_error('ignore', lambda exc: (u'', exc.end))
        self.assertEqual(strict_decode(b'\xff'), ('
