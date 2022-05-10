import ctypes
# Test ctypes.CField

if __name__ == "__main__":
    import sys
    import test.test_support
    verbose = test.test_support.verbose
    if verbose:
        print "testing ctypes"
    from ctypes import *
    from ctypes.test import need_symbol
    if need_symbol("union u"):
        class U(Union):
            _fields_ = [("a", c_int),
                        ("b", c_char * 4)]
    else:
        class U(Union):
            _fields_ = [("a", c_int),
                        ("b", c_int)]

    class S(Structure):
        _fields_ = [("u", U),
                    ("c", c_char)]

    s = S()
    if verbose:
        print s.u.a
        print repr(s.u.b)
        print repr(s.c)
    s.u.a = -1
    s.u.b = "abc"
    s.c = "X"
    if verbose:
        print
