import codecs
# Test codecs.register_error()
import codecs

def handler(exception):
    return (u'\uFFFD', exception.end)

codecs.register_error('test', handler)

# Test codecs.lookup_error()
import codecs

def handler(exception):
    return (u'\uFFFD', exception.end)

codecs.register_error('test', handler)

codecs.lookup_error('test') == handler

# Test codecs.strict_errors()
import codecs

def handler(exception):
    return (u'\uFFFD', exception.end)

codecs.register_error('test', handler)

codecs.lookup_error('test') == handler

