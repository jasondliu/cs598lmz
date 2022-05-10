import codecs
# Test codecs.register_error
import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('my.error', handler)

# Test codecs.lookup_error
import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('my.error', handler)

assert codecs.lookup_error('my.error') is handler

# Test codecs.strict_errors
import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('my.error', handler)

assert codecs.lookup_error('my.error') is handler

# Test codecs.replace_errors
import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('my.error', handler)

assert codecs.lookup_error('my.error') is handler

# Test codecs.ignore_errors
import codecs


