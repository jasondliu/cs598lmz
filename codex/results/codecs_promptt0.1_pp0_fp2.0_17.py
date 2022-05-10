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
for encoding in ['ascii', 'latin-1', 'utf-8']:
    for errors in ['strict', 'ignore', 'replace', 'test.bad_decode']:
        print encoding, errors
        print codecs.decode('abc', encoding, errors)
        print codecs.encode('abc', encoding, errors)

# Test the error handler with a unicode argument
for encoding in ['ascii', 'latin-1', 'utf-8']:
    for errors in ['strict', 'ignore', 'replace', 'test.bad_encode']:
        print encoding, errors
        print codecs.decode(u'abc', encoding
