import codecs
# Test codecs.register_error()

import encodings.latin_1

def my_replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def test_main():
    # This test is not very thorough.
    # XXX add more tests
    codecs.register_error("my_replace", my_replace_error)
    #
    s = '\x80abc\xff'
    assert unicode(s, "latin-1", "replace") == u'\ufffdabc\ufffd'
    assert unicode(s, "latin-1", "my_replace") == u'\ufffdabc\ufffd'
    #
    assert unicode(s, "latin-1", "strict") == u'\ufffdabc\ufffd'
    #
    assert unicode(s, "latin-1", "ignore") == u'abc'
    #
