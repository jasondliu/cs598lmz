import codecs
# Test codecs.register_error, #8136
# http://bugs.python.org/issue8136

def dummy_decode(input, errors='strict'):
    return (u'\ufffd', len(input))

codecs.register_error('test.dummy_decode', dummy_decode)

import encodings.iso8859_3

def test_main():
    s = '\xab'
    for encoding in ('iso8859_3', 'iso8859-3', 'latin3', 'Latin-3'):
        for errors in ('strict', 'ignore', 'replace', 'test.dummy_decode'):
            print encoding, errors
            assert codecs.decode(s, encoding, errors) == u'\ufffd'
            
    # check that the emulated error handler is indeed used
    assert codecs.decode(s, 'iso8859_3', 'test.dummy_decode') == u'\ufffd'
    assert codecs.decode(s, 'iso8859_3', 'test.dummy_dec
