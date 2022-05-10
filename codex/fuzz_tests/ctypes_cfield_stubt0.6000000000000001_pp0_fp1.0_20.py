import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def g():
    print(ctypes.CField)

def f():
    print(ctypes.CField)
    g()

f()
""")

test.run_one('-b')

test.must_match('out.so', "abc\nabc\n")

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
