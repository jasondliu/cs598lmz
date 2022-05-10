import codecs
# Test codecs.register_error

import codecs
import test.test_support
import StringIO

class UnprintableError(UnicodeError):
    def __init__(self, object):
        self.object = object
    def __str__(self):
        return '<unprintable %s object>' % type(self.object).__name__

def errhandler(error):
    raise UnprintableError(error.object)

def test(encoding):
    codecs.register_error("test", errhandler)

    for i in range(0xD800, 0xDC00):
        s = unichr(i)
        try:
            s.encode(encoding, "test")
        except UnprintableError:
            pass
        else:
            raise AssertionError("should raise UnprintableError")

    try:
        u"\U00010000".encode(encoding, "test")
    except UnicodeEncodeError:
        # surrogateerror error
        pass
    else:
        raise AssertionError("should raise UnicodeEncodeError")


