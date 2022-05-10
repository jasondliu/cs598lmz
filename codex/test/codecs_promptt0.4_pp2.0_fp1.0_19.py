import codecs
# Test codecs.register_error()

import codecs
import encodings

class MyLookupError(LookupError):
    pass

def my_lookup(encoding):
    if encoding == 'test.notfound':
        raise MyLookupError
    return encodings.search_function(encoding)

def my_register_error(errors):
    def my_lookup_error(name):
        if name == 'test.lookuperror':
            raise LookupError
        return errors(name)
    return my_lookup_error

def my_strict_errors(exception):
    raise exception

def my_ignore_errors(exception):
    return (u'', 1)

def my_replace_errors(exception):
    return (u'?', 1)

def my_xmlcharrefreplace_errors(exception):
    return (u'&#%d;' % ord(exception.object[exception.start]),
            exception.end)

