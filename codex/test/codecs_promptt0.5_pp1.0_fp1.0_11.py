import codecs
# Test codecs.register_error, #8136
# http://bugs.python.org/issue8136

def dummy_decode(input, errors='strict'):
    return (u'\ufffd', len(input))

codecs.register_error('test.dummy_decode', dummy_decode)

import encodings.iso8859_3

def test_main():
    s = '\xab'
