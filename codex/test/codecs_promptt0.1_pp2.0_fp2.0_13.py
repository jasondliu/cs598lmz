import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.replace', handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.backslashreplace', handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.namereplace', handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

def handler(exception):
    return (u'', exception.end)

