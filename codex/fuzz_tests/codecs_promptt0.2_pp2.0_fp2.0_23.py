import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

for encoding in ('ascii', 'latin-1', 'utf-8'):
    print encoding
    try:
        u'\N{SNOWMAN}'.encode(encoding, 'test.bad_encode')
    except UnicodeError:
        print 'UnicodeError'
    try:
        '\xe2\x98\x83'.decode(encoding, 'test.bad_decode')
    except UnicodeError:
        print 'UnicodeError'

# Test codecs.lookup

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='st
