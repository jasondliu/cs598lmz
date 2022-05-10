import codecs
# Test codecs.register_error
def raiseok(exc):
    uc = exc.object[exc.start]
    if uc == u'\xab':
        exc.end = exc.start+1
        return u'abc'
    if uc == u'\x20':
        exc.end = exc.start+1
        return u''
    if uc == u'\s':
        exc.end = exc.start+1
        return u' '
    if uc == u'\tabc':
        exc.end = exc.start+1
        return u' '
    raise TypeError, 'doh!'

def encodeok(uc):
    if uc == u'A':
        return 'Abc'
    return codecs.charmap_encode(uc, 'strict', encoding_map)

def reencodeok(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError, "don't know how to handle %r" % exc
    if not exc.object.endswith(u'\uabcd'):
