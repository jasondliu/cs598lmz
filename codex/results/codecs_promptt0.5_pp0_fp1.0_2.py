import codecs
# Test codecs.register_error()

def handler(exception):
    print 'got', exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test', handler)

for encoding in ['ascii', 'iso8859_10']:
    print 'Encoding:', encoding
    text = u'pi: \u03c0'
    print 'Original:', repr(text)
    # Encode as bytes
    encoded = text.encode(encoding, 'test')
    print 'Encoded :', repr(encoded)
    # Decode to unicode
    decoded = encoded.decode(encoding, 'test')
    print 'Decoded :', repr(decoded)
    print

'''
Encoding: ascii
Original: u'pi: \u03c0'
got UnicodeEncodeError
Encoded : 'pi: \xcf\x80'
got UnicodeDecodeError
Decoded : u'pi: \xcf\x80'

Encoding: iso8859_10
Original: u
