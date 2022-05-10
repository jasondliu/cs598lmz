import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_fielddescriptor(self, module=None):
        # Normally in Python 2, it's enough to access an attribute
        # to trigger the __get__ method on descriptor objects.  But
        # this is not true for _ctypes.CField objects:  At least in
        # Python 2.7, __get__ is not called when they are accessed as
        # module-level data.  To get around this, we set the 'module'
        # member of the descriptor, after which the interpreter will
        # call __get__.
        s = S()
        x = S.x
        try:
            x.__get__(s)
        except TypeError:
            # We're the master under Python 2, and the expected code is
            # not executed, because the field is accessed as module global
            # data.  So force the interpreter to call __get__.
            self.assertIsNone(x.__module__)
            x.__module__ = '__FAKE__'
            s = super(type(s
