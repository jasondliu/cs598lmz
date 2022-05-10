import ctypes
# Test ctypes.CField instance is used by ctypes.POINTER


class POINTER(object):
    _type_ = 'i'

    def __init__(self, *args):
        pass

    def from_param(self, param):
        if param is None:
            return param
        else:
            return param._ptr


def test(testspec):
    import _ctypes_test
    lib = ctypes.CDLL(_ctypes_test.__file_)
    try:
        func = getattr(lib, 'my_' + testspec.replace(':', '_'))
    except AttributeError:
        func = _ctypes_test.expect_success[testspec] and lib.raise_exception or lib.cause_segfault

    TP = type(POINTER(ctypes.c_int)())
    CFIELD = ctypes.CField
    try:
        f = CFIELD('_obj', None, TP)
        ctypes.CFUNCTYPE(None, type(f))(func)
    except:
        if _ctypes_test.
