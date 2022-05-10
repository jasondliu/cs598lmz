import codecs
# Test codecs.register_error

import codecs

def bad_errorhandler(exception):
    raise TypeError

def good_errorhandler(exception):
    return (u'', exception.end)

codecs.register_error('test.bad', bad_errorhandler)
codecs.register_error('test.good', good_errorhandler)

# Encoding
for encoding in ['test.bad', 'test.good']:
    try:
        codecs.charmap_encode(u'\u3042', encoding, 'strict')
    except TypeError:
        print('TypeError raised with %s' % encoding)
    else:
        print('No exception raised with %s' % encoding)

# Decoding
for encoding in ['test.bad', 'test.good']:
    try:
        codecs.charmap_decode(b'\x00', encoding, 'strict')
    except TypeError:
        print('TypeError raised with %s' % encoding)
    else:
        print('No exception raised with %s' % encoding)
