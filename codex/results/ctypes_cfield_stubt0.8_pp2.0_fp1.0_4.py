import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def sorted(lst):
    lst = list(lst)
    lst.sort()
    return lst

def shorten(value, min=32):
    s = repr(value)
    if len(s) <= min:
        return s
    if isinstance(value, basestring):
        return s[:min-3] + '...'
    return s[:min-3] + '...' + hex(id(value))

def format_ctype(ctype):
    return str(ctype).split("'")[1]

def have_docstrings():
    # PyPy doesn't have docstrings on the types yet
    return hasattr(ctypes.c_int, '__doc__')

class BaseTest(unittest.TestCase):
    def assertEquals(self, x, y):
        if x != y:
            x = shorten(x)
            y = shorten(y)
        unittest.TestCase.assertEquals(self, x, y)

    def assertTrue(self, expr):

