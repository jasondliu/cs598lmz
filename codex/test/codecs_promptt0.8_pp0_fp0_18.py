import codecs
# Test codecs.register_error


def lookup_error_function(name):
    """Create a lookup error function that looks up the name in globals()."""
    def f(encoding):
        return globals()[name]
    return f


def test_utf8_surrogates(self):
    # Test the register_error mechanism with utf-8
    text = "\xe9\u0100"
    self.assertRaises(UnicodeEncodeError, text.encode, 'utf-8')
    codecs.register_error('test.surrogateescape', lookup_error_function('surrogateescape_error'))
    self.assertEqual(text.encode('utf-8', 'test.surrogateescape'), b'\xe9\x80')
    codecs.register_error('test.surrogatepass', lookup_error_function('surrogatepass_error'))
