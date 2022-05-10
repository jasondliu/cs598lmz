import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)
import locale
import struct
import sys
import unittest
import warnings
from test import support
from test.support import TESTFN, requires_resource, import_module

def _encode(errors, encoding, text, bufsize=0, expected=None):
    if expected is None:
        expected = text
    try:
        f = codecs.getencoder(encoding)
    except LookupError:
        if encoding == '__test_unknown_encoding__':
            return expected
        raise
    if bufsize == 0:
        return f(text, errors)[0]
    else:
        res = ''
        for i in range(0,
