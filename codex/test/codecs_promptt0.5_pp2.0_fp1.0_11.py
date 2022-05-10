import codecs
# Test codecs.register_error
# - should raise a TypeError if the first argument is not a string
# - should raise a TypeError if the second argument is not a callable
# - should raise a LookupError if the error handler is already registered
# - should register the error handler if the error handler is not already registered

def handler_pass(exception):
    pass

def handler_return(exception):
    return u'x'

def handler_replace(exception):
    return (u'x', exception.end)

def handler_xmlcharrefreplace(exception):
    return (u'&#%d;' % ord(exception.object[exception.start]), exception.end)

def handler_backslashreplace(exception):
    return (u'\\u%04x' % ord(exception.object[exception.start]), exception.end)

def handler_namereplace(exception):
    return (u'\\N{%s}' % unicodedata.name(exception.object[exception.start]), exception.end)

