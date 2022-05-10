import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def _test(name, value):
    try:
        fields = [
            (name, ctypes.CField(value)),
            ("a", ctypes.c_int)]

        S._fields_ = fields
    except TypeError:
        pass

_test('\U0001f3c3', '')
_test('\U0001f3c3', '\U0001f3c3')
_test('\U0001f3c3', '\U0001f3c3\U0001f3c3')
_test('\U0001f3c3\U0001f3c3', '\U0001f3c3\U0001f3c3')
_test('\U0001f3c3\U0001f3c3', '')
_test('\U0001f3c3\U0001f3c3', '\U0001f3c3')
"""
    # This should *not* SEGV
    output = run('-c', source)


@pytest.mark.skipif(not IS_CPYTHON,
                    reason
