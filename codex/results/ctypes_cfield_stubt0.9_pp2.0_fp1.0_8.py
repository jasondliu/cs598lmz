import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # for mypy 3 support

if sys.version_info[0] > 2:
    import unicodedata
    chr = chr # for mypy 3 support
    unichr = chr

    def u(s):
        return s

    def b(s):
        return s.encode('latin-1')

    def bytes(n):
        return bytes(bytearray(n))
else:
    import unicodedata

    unichr = unichr
    chr = chr

    def u(s):
        return unicode(s, "unicode_escape")

    def b(s):
        return s


class Dummy:
    pass


def _check(name, f):
    def check(self):
        f(self)
    return check


def make_checker(name, f):
    def fail(self, e):
        raise self.failureException(e)

    def check(self):
        try:
            f()
        except self.failureException:
            raise
        except Exception as e
