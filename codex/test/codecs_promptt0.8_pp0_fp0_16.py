import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'@', exception.start + 1)

def reader(stream, errors='strict'):
    return codecs.StreamReader(stream, errors, handler)

