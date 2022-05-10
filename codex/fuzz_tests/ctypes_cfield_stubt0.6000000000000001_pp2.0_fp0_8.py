import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(msg, *args):
    print('-' * 60)
    print(msg)
    for func, expected in args:
        result = func()
        print('%s.__name__ = %r' % (func.__name__, result))
        assert result == expected, 'expected %r' % (expected,)

def test_normal_fields():
    test('normal fields',
         (lambda: S.x.__name__, 'x'),
         )

def test_unnamed_fields():
    f = ctypes.c_int * 3
    test('unnamed fields',
         (lambda: f.__name__, 'c_int_Array_3'),
         )

def test_unnamed_fields_with_offset():
    f = ctypes.c_int * 3
    test('unnamed fields with offset',
         (lambda: f.__name__, 'c_int_Array_3'),
         )

def test_anonymous_struct():
    class S(ctypes.Structure):
        pass
    test('an
