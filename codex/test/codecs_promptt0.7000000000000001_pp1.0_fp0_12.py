import codecs
# Test codecs.register_error()

def strict_error(exception):
    return (None, exception.end)

def ignore_error(exception):
    return (u'', exception.end)

def replace_error(exception):
    return (u'\ufffd', exception.end)

def xmlcharrefreplace_error(exception):
    return (u'&#%d;' % ord(exception.object[exception.start:exception.end]),
            exception.end)

def backslashreplace_error(exception):
    return (u'\\x%02x' % ord(exception.object[exception.start:exception.end]),
            exception.end)

def namereplace_error(exception):
    name = exception.encoding
    if name == 'ascii':
        name = 'latin-1'
    return (u'&%s;' % unicodedata.name(exception.object[exception.start:exception.end],
                                       name),
            exception.end)

