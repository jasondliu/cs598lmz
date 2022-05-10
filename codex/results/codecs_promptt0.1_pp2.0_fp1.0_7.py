import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler:", exception
    return (u'', exception.end)

def my_ignore_error_handler(exception):
    print "my_ignore_error_handler:", exception
    return (u'', exception.end)

def my_replace_error_handler(exception):
    print "my_replace_error_handler:", exception
    return (u'x', exception.end)

def my_xmlcharrefreplace_error_handler(exception):
    print "my_xmlcharrefreplace_error_handler:", exception
    return (u'&#%d;' % ord(exception.object[exception.start]), exception.end)

def my_backslashreplace_error_handler(exception):
    print "my_backslashreplace_error_handler:", exception
    return (u'\\x%02x' % ord(exception.object[exception.start]), exception.end)

def my_namereplace_error_
