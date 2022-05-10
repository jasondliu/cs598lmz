import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError("bad decode")

def bad_encode(input, errors='strict'):
    raise UnicodeError("bad encode")

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

# Test decoding

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding
    try:
        u = unicode('\xff', encoding, 'test.bad_decode')
    except UnicodeError, err:
        print 'UnicodeError:', err
    else:
        print 'no exception'

# Test encoding

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding
    try:
        s = u'\uffff'.encode(encoding, 'test.bad_encode')
    except UnicodeError, err:
        print 'Un
