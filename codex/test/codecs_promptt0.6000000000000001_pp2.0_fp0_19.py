import codecs
# Test codecs.register_error
def handler(exception):
    return u"", exception.end
codecs.register_error("test.my_error", handler)
def my_xmlcharrefreplace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u"&#%d;" % ord(exc.object[idx]) for idx in range(exc.start, exc.end)]
        return u"".join(s), exc.end
    else:
        raise TypeError("don't know how to handle %r" % exc)
codecs.register_error("xmlcharrefreplace", my_xmlcharrefreplace)

# Test encodings
