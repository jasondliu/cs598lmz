import ctypes
# Test ctypes.CField and all kinds of array fields.
from ctypes.test.test_structures import _test

try:
    # cStringIO.StringIO, StringIO.StringIO objects are file-like,
    # but do not have all the attributes necessary for ctypes.
    import cStringIO
except ImportError:
    class cStringIO:
        pass

try:
    import StringIO
except ImportError:
    class StringIO:
        pass

class _CDataIO(ctypes._SimpleCData, file):
    _type_ = "l"
    def __init__(self, other=None, **kw):
        if isinstance(other, (int, long)):
            f = open(other, **kw)
            self.value = f.fileno()
        elif not isinstance(other, (str, unicode)):
            f = other
            self.value = f.fileno()
        else:
            f = open(other, **kw)
            self.value = f.fileno()
        file.__init__(self, f.fileno
