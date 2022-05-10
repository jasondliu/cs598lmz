import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test_decode():
    for errors in ['strict', 'ignore', 'replace', 'test.bad_decode']:
        for encoding in ['ascii', 'latin-1', 'utf-8']:
            try:
                u = 'abc'.decode(encoding, errors)
            except UnicodeError:
                if errors == 'test.bad_decode':
                    pass
                else:
                    raise
