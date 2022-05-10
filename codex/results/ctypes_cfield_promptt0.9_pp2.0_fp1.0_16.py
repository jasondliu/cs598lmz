import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        (1, ctypes.c_char*9)
    ]
C()


# Test more ctypes code
# Issue 490465
try:
    import ctypes
except ImportError:
    ctypes = None
MSVCRT = ctypes and ctypes.CDLL('msvcrt')
if MSVCRT is not None:
    # non-existent function
    pytest.raises(AttributeError, lambda: MSVCRT.foo())
    # _putch: a callable
    # Argument type information is not recognized by ctypes, so
    # _putch gets called with the wrong argument. On 64-bit MSVCRT,
    # the wrong argument causes a crash.
    if MSVCRT._putch(0) == -1:
        pytest.skip('MSVCRT._putch() failed, skipping test_crash')
    # _memicmp: an integer
    assert MSVCRT._memicmp
