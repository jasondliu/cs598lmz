import ctypes
# Test ctypes.CFUNCTYPE for all return types.
import _ctypes_test


def test_primitive_types():
    for tp in 'short', 'int', 'long', 'longlong', 'float', 'double':
        f = getattr(_ctypes_test, 'test_' + tp)
        func = CFUNCTYPE(eval(tp))(f)
        assert func() == f()


def test_structures():
    class X(Structure):
        _fields_ = [('a', c_int)]

    class Y(Structure):
        _fields_ = [('a', c_int), ('b', c_int)]

    class Z(Union):
        _fields_ = [('a', c_char), ('b', c_int)]

    for tp in X, Y, Z:
        f = getattr(_ctypes_test, 'test_' + tp.__name__)
        func = CFUNCTYPE(tp)(f)
        assert func().a == f().a


def test_pointers():
    for tp in c_char
