import codecs
# Test codecs.register_error()
# First, get a utf-8 encoding with xmlcharrefreplace error
def xmlcharreplace(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u''.join(u'&#%d;' % ord(c) for c in exc.object[exc.start:exc.end]),
            exc.end)
codecs.register_error("test.xmlcharrefreplace", xmlcharreplace)
utf8_xmlcharrefreplace = codecs.getencoder("utf-8" + codecs.BOM_UTF8 + "test.xmlcharrefreplace")
# Then, get a utf-8 encoding with backslashreplace error
utf8_backslashreplace = codecs.getencoder("utf-8" + codecs.BOM_UTF8 + "backslashreplace")
# Test that the right error handler is called
test_string = u'\u1234'
assert utf8_xmlcharrefreplace(test_string)[0] == b'
