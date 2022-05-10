import codecs
# Test codecs.register_error()

def handler(exception):
    """Handle encoding and decoding errors by replacing unencodable chars."""
    return (u'\ufffd', exception.start + 1)

# Register the error handler for all encodings
codecs.register_error('test.replace', handler)

# Encode a unicode string with a known encoding error
s = u'abcd\udce2\udcfe'
print s

encoding = 'ascii'
print 'Encoding:', encoding

# For unicode object, use 'name' error handler
print s.encode(encoding, 'test.replace')

# For strings, use a lookup function
print codecs.encode(s, encoding, 'test.replace')

# Decode a byte string with a known decoding error
s = 'abcd\x80\xfe'
print repr(s)

# For byte strings, use a lookup function
print repr(codecs.decode(s, encoding, 'test.replace'))

# Unicode warnings can be suppressed like this
import warnings
with
