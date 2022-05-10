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
