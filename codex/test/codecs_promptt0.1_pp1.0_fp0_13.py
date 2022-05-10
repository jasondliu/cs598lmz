import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

# Test the error handler

for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
    try:
        u'\u1234'.encode(encoding, 'test.bad_encode')
    except UnicodeError:
        pass
    else:
        print('Failed to raise UnicodeError for encoding', encoding)

for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
    try:
        b'\xff'.decode(encoding, 'test.bad_decode')
    except UnicodeError:
        pass
