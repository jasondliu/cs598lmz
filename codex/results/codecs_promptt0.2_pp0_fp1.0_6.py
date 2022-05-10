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

def test_bad_decode():
    for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le',
                     'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be']:
        try:
            codecs.decode(b'\xff', encoding, errors='test.bad_decode')
        except UnicodeError:
            pass
        else:
            raise AssertionError("should have raised UnicodeError")

def test_bad_encode():
    for encoding in ['ascii', 'latin-1', 'utf-8',
