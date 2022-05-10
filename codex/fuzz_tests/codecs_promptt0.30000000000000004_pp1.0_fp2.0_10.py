import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def strict_errorhandler(exception):
    raise_exc(exception)

def ignore_errorhandler(exception):
    return (u'', exception.end)

def replace_errorhandler(exception):
    return (u'\ufffd', exception.end)

def xmlcharrefreplace_errorhandler(exception):
    return (u'&#%d;' % ord(exception.object[exception.start]), exception.end)

def backslashreplace_errorhandler(exception):
    return (u'\\x%02x' % ord(exception.object[exception.start]), exception.end)

def namereplace_errorhandler(exception):
    return (u'\\N{REPLACEMENT CHARACTER}', exception.end)

def xmlcharrefreplace_errorhandler(exception):
    return (u'&#%d;' % ord(exception.object[exception.start]), exception.end)

def backslashreplace
