import codecs
# Test codecs.register_error.

import codecs
import unittest
try:
    set
except NameError:
    from sets import Set as set

roundtrip_error_char = "¥"

def gen_test_encoding_map(map, errors='strict', roundtrip_error=False):
    codecs.register_error(errors, lambda e: (u'<%s>' % e.object[e.start], e.end))
    if roundtrip_error:
        map = map.replace(roundtrip_error_char, '¥')
    codecs.register(lambda name: codecs.lookup('string_escape') if name == 'test' else None)
    yield '', "\"test\" codec isn't available", 'test'
    yield [roundtrip_error_char], [u'<\\x00>', u'<\\x00>', u'<\\x00>', roundtrip_error_char], 'test', errors

#     deprecated version of the same encoder, should have the same result
