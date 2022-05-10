import codecs
# Test codecs.register_error
import encodings.latin_1

def hexescape(exc):
    s = exc.object[exc.start:exc.end]
    return (u'\\x' + u'\\x'.join([hex(ord(c))[2:] for c in s]),
            exc.end)

codecs.register_error('hexescape', hexescape)

def hexescape_decode(s, errors='strict'):
    return s.decode('latin-1', errors), len(s)

def hexescape_encode(s, errors='strict'):
    return s.encode('latin-1', errors), len(s)

