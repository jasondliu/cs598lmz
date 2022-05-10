import codecs
# Test codecs.register_error

import warnings
import functools

# For testing UnicodeDecodeError and UnicodeEncodeError
class MyUnicodeError(UnicodeError):
    def __init__(self, obj, *args):
        self.object = obj
        UnicodeError.__init__(self, *args)

    def __str__(self):
        return 'MyUnicodeError(%r, %s)' % (self.object,
                                           UnicodeError.__str__(self))

class MyLookupError(LookupError):
    def __init__(self, obj, *args):
        self.object = obj
        LookupError.__init__(self, *args)

    def __str__(self):
        return 'MyLookupError(%r, %s)' % (self.object,
                                          LookupError.__str__(self))

def strict_errors(exc):
    raise MyUnicodeError(exc.object, *exc.args)

