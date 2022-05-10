import codecs
# Test codecs.register_error, with a custom error handler.
# This is a test for SF bug #813894: codecs.register_error()
# doesn't work with codecs.escape_decode()

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('strict', my_error_handler)

# this should not raise an exception
codecs.escape_decode('\x80', 'strict')

# this should raise an exception
