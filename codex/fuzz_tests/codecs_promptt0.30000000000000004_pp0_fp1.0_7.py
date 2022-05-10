import codecs
# Test codecs.register_error
import codecs

def handler(exception):
    print 'Handling %s' % exception.__class__.__name__
    return (u'', exception.start + 1)

codecs.register_error('test.lookup', handler)

# Encode a unicode string with a known codec
encoded = u'pi: \u03c0'.encode('ascii', 'test.lookup')
print 'Encoded:', encoded

# Decode an 8-bit string with a known codec
decoded = encoded.decode('ascii', 'test.lookup')
print 'Decoded:', decoded

# Encode a unicode string with an unknown codec
try:
    encoded = u'pi: \u03c0'.encode('no-such-codec', 'test.lookup')
except LookupError, err:
    print 'ERROR:', err

# Decode an 8-bit string with an unknown codec
try:
    decoded = encoded.decode('no-such-codec', 'test.lookup')
except
