import codecs
# Test codecs.register_error,
import test.test_codecs
from test import test_support

# Import uuid to ensure that the Python implementation is loaded
import uuid


class MyUUID(uuid.UUID):
    def __new__(cls, hex='00000000000000000000000000000000', version=4):
        obj = uuid.UUID.__new__(cls, hex, version)
        return obj

def test_error_callback():
    def raise_exception(*args):
        raise TypeError
    def ignore_exception(*args):
        return (u'', 0)
    codecs.register_error('test.raise_exception', raise_exception)
    codecs.register_error('test.ignore_exception', ignore_exception)
    s = u'\x00\xff'
    try:
        unicode(s, 'ascii', 'test.raise_exception')
    except TypeError:
        pass
    else:
        raise TestFailed('expected TypeError')
    unicode(s, 'ascii', 'test.ignore_ex
