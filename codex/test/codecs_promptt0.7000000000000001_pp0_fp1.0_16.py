import codecs
# Test codecs.register_error()

def handler(exception):
    """Handle encoding and decoding errors by replacing unencodable chars."""
    return (u'\ufffd', exception.start + 1)

# Register the error handler for all encodings
codecs.register_error('test.replace', handler)

# Encode a unicode string with a known encoding error
s = u'abcd\udce2\udcfe'
