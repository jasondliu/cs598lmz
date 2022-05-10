import codecs
# Test codecs.register_error
import os
from test import support

# Decoding with "replace"
def test_replace_1():
    def f(exc):
        if isinstance(exc, UnicodeDecodeError):
            return ('?', exc.end)
        raise TypeError
    codecs.register_error("test.replace", f)
    assert 'abc\uffffdef'.decode('ascii', 'test.replace') == 'abc?def'

# Encoding with "replace"
def test_replace_2():
    def f(exc):
        if isinstance(exc, UnicodeEncodeError):
            return ('?', exc.end)
        raise TypeError
    codecs.register_error("test.replace", f)
    assert u'abc\uFFFFdef'.encode('ascii', 'test.replace') == 'abc?def'

# Decoding with "ignore"
def test_ignore_1():
    def f(exc):
        if isinstance(exc, UnicodeDecodeError):
            return ('', exc.end)
        raise TypeError
    codecs.
