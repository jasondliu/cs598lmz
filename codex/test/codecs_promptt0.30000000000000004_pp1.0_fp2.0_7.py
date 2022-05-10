import codecs
# Test codecs.register_error

import codecs
import sys

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

class Test:
    def test_register_error(self):
        # Test the register_error function
        # The error handler should be called with a UnicodeEncodeError
        # instance having a reason attribute
        def bad_handler(exception):
            if not isinstance(exception, UnicodeEncodeError):
                raise TypeError("don't know how to handle %r" % exception)
            if not hasattr(exception, 'reason'):
                raise AttributeError("reason missing")
            return (u'', exception.end)
        codecs.register_error('test.unicode', bad_handler)
        u = u'\u3042'
        try:
            u.encode('test.unicode')
        except UnicodeEncodeError as e:
            if e.reason != 'test.unicode':
                raise
