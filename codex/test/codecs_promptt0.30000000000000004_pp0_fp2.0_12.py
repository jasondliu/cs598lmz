import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

