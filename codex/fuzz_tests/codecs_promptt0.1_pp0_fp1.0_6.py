import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

# Test that the error handler is called
for encoding in ['ascii', 'latin-1', 'utf-8']:
    try:
        codecs.decode('\xff', encoding, 'test.bad_decode')
    except UnicodeError:
        pass
    else:
        print('UnicodeError not raised')

for encoding in ['ascii', 'latin-1', 'utf-8']:
    try:
        codecs.encode('\xff', encoding, 'test.bad_encode')
    except UnicodeError:
        pass
    else:
        print('UnicodeError not raised')

# Test that the error handler is not called
for encoding
