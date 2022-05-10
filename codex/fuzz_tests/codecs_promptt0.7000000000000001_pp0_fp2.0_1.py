import codecs
# Test codecs.register_error.

import codecs
import sys

def encoder(s):
    return s.upper(), len(s)

def decoder(s):
    return s.lower(), len(s)

codecs.register_error('test', encoder, decoder)

def test_str(s):
    try:
        b = s.encode('ascii', 'test')
    except UnicodeEncodeError as err:
        print(err)
    else:
        print(repr(b))
        print(b.decode('ascii', 'test'))
        print()

for s in ['abc', '\xe9', '\xe9\x99\xa0', '\xe9\x99\xa0\xff']:
    test_str(s)

# Test replacement_characters.

import codecs, sys

replacements = sys.maxunicode + 1

def encoder(s):
    return '', 0

def decoder(s):
    return '?', 1

codecs.register_
