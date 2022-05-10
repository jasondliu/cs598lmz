import codecs
# Test codecs.register_error()
def my_replace(exc):
    return (u'X', 1)

codecs.register_error('my_replace', my_replace)

s = u'\uFFFD'
s2 = s.encode('ascii', 'my_replace')
assert s2 == b'X'

s = u'\uFFFDx'
s2 = s.encode('ascii', 'my_replace')
assert s2 == b'Xx'

s = u'\uFFFD'
s2 = s.encode('ascii', 'my_replace')
assert s2 == b'X'

s = u'\uFFFDx'
s2 = s.encode('ascii', 'my_replace')
assert s2 == b'Xx'

import binascii

def my_replace_bin(exc):
    return (binascii.unhexlify(b'00'), 1)

codecs.register_error('my_replace_bin', my_replace_bin)


