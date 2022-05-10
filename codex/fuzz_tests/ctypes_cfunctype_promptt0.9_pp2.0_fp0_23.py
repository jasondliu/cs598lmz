import ctypes
# Test ctypes.CFUNCTYPE on a variadic function.
# Also test ctypes.strerror
#
# The prototype:
# int py_printf(const char *fmt, ...);

libc = ctypes.CDLL(ctypes.util.find_library("c"))

_va_functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.va_list)
py_printf = _va_functype(("vprintf", libc), (ctypes.c_char_p,))

def py_printf_test():
    res = py_printf('Some %s %d %c string', ctypes.c_char_p('test'),
                    ctypes.c_int(42), ctypes.c_char('C'))
    assert res == 10, "returned value was %d" % res

    try:
        py_printf(ctypes.c_char_p('This is no %s'))
    except TypeError, e:
        assert "Required argument 'fmt' (pos 1) not
