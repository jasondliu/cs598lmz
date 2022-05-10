import codecs
# Test codecs.register_error

def handler(exception):
    return (u'\ufffd', exception.end)

def test_main():
    def test(encoding):
        handler_called = 0
        u = u'caf\xe9'
        for errors in ['strict', 'replace', 'ignore', 'backslashreplace',
                       'xmlcharrefreplace', 'namereplace', 'surrogateescape']:
            if errors == 'surrogateescape' and not hasattr(codecs, 'surrogateescape_decode'):
                continue
            if errors == 'namereplace' and not hasattr(codecs, 'namereplace_decode'):
                continue
            try:
                s = u.encode(encoding, errors)
            except UnicodeEncodeError:
                pass
            else:
                codecs.register_error(errors, handler)
                try:
                    r = s.decode(encoding, errors)
                except UnicodeDecodeError:
                    pass
