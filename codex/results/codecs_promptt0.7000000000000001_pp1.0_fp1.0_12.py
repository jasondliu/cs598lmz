import codecs
# Test codecs.register_error
# Test the 'backslashreplace' error handler.

import codecs, sys

def test(text, encoding):
    print(repr(text))
    print(repr(codecs.escape_encode(text)[0]))
    print(repr(codecs.escape_decode(codecs.escape_encode(text)[0])[0]))
    print(repr(codecs.escape_decode(codecs.escape_encode(text)[0], 'strict')[0]))
    print(repr(text.encode(encoding, 'backslashreplace')))
    print(repr(text.encode(encoding, 'backslashreplace').decode(encoding)))
    print(repr(text.encode(encoding, 'backslashreplace').decode(encoding, 'strict')))
    print(repr(text.encode(encoding, 'backslashreplace').decode(encoding, 'replace')))
    print(repr(text.encode(encoding
