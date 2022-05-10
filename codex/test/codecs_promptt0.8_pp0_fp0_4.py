import codecs
# Test codecs.register_error
def handler_ignore(exception):
    return (u"", exception.end)
codecs.register_error("test.ignore", handler_ignore)

def handler_replace(exception):
    return (u"?", exception.end)
codecs.register_error("test.replace", handler_replace)

def handler_xmlcharrefreplace(exception):
    return (u"&#%d;" % ord(exception.object[exception.start]), exception.end)
codecs.register_error("test.xmlcharrefreplace", handler_xmlcharrefreplace)

def handler_backslashreplace(exception):
    return (u"\\x%02x" % ord(exception.object[exception.start]), exception.end)
codecs.register_error("test.backslashreplace", handler_backslashreplace)

def handler_codec_error(exception):
    return (u"E", exception.end)
codecs.register_error("test.codec_error", handler_codec_error)

