import codecs
# Test codecs.register_error()

import codecs, encodings.utf_8

def handler(ex):
    print 'handler called with', ex
    return u'\ufffd', ex.end

codecs.register_error('custom-utf-8', handler)

# test #1: no surrogate
s = '\xe4\xbd\xa0\xe5\xa5\xbd'
u = u'\u4f60\u597d'
assert codecs.utf_8_decode(s, 'custom-utf-8') == (u, len(s))
assert codecs.utf_8_encode(u, 'custom-utf-8') == (s, len(u))

# test #2: one surrogate
s += '\xed\xa0\x80'
u += u'\ud800'
assert codecs.utf_8_decode(s, 'custom-utf-8') == (u, len(s))

# test #3: two surrogates
s += '\xed\xb0\x80'
u += u'
