import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_decode)
codecs.register_error('test.bad', bad_encode)

# Test the error handler
for encoding in ['ascii', 'latin-1', 'utf-8']:
    try:
        u'\u1234'.encode(encoding, 'test.bad')
    except UnicodeError:
        pass
    else:
        print('encoding', encoding, 'did not raise UnicodeError')

for encoding in ['ascii', 'latin-1', 'utf-8']:
    try:
        b'\xff'.decode(encoding, 'test.bad')
    except UnicodeError:
        pass
    else:
        print('encoding', encoding, 'did not raise UnicodeError')

# Test the error handler with a non-UnicodeError exception

