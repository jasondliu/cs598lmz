import codecs
# Test codecs.register_error
def xmlcharrefreplace_error(exc):
    """Test error handler for codecs.register_error"""
    if isinstance(exc, UnicodeEncodeError):
        s = ["&#%d;" % ord(c) for c in exc.object[exc.start:exc.end]]
        return (u''.join(s), exc.end)
    else:
        return codecs.xmlcharrefreplace_error(exc)

codecs.register_error("test.xmlcharrefreplace", xmlcharrefreplace_error)

def test_main():
    text = u'A\u0dcaB\u0dcaC'
    expect = u'A&#3514;B&#3514;C'
    result = text.encode("ascii", "xmlcharrefreplace")
