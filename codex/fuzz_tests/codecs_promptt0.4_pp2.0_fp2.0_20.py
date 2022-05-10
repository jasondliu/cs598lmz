import codecs
# Test codecs.register_error()

def register_error(encoding):
    def handler(exc):
        if isinstance(exc, UnicodeDecodeError):
            return (u'\ufffd', exc.end)
        raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error(encoding, handler)

def test_main():
    for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le',
                     'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be']:
        register_error(encoding)
        s = '\x80'
        if encoding.startswith('utf-16'):
            s = '\x00\x80'
        elif encoding.startswith('utf-32'):
            s = '\x00\x00\x00\x80'
        for errors in ['strict', 'replace', 'ignore']:
            print encoding, errors
            t = unicode(s, encoding
