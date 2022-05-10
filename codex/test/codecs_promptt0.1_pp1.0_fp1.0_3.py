import codecs
# Test codecs.register_error

import codecs

def my_error(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error)

