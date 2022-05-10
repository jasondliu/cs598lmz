import codecs
# Test codecs.register_error
import codecs
def bad_decode_handler(ex):
    return (u'/xFF', ex.end)
codecs.register_error('bad-decode', bad_decode_handler)
codecs.register_error('bad-decode', bad_decode_handler)
s = codecs.decode('\xff', 'ascii', 'bad-decode')
assert s == u'/xFF'
# Test codecs.lookup_error
import codecs
def bad_decode_handler(ex):
    return (u'/xFF', ex.end)
codecs.register_error('bad-decode', bad_decode_handler)
handler = codecs.lookup_error('bad-decode')
assert handler(UnicodeEncodeError('', u'', 0, 1, 'bad-decode')) == (u'/xFF', 1)
# Test codecs.lookup
import codecs
assert codecs.lookup('utf8') is codecs.utf_8_encode
assert codecs.lookup('utf-
