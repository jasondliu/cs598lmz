fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# fn.__code__.co_argcount varies by platform:
# CPython:  3 (fn, self, args)
# MicroPython: 5 (fn, self, module, module.__name__[0], args)

# pyc files are magic bytes followed by a 4 byte version number, followed by
# timestamp, followed by marshalled code object.
#
# https://docs.python.org/3.6/reference/datamodel.html#index-76
# https://www.python.org/dev/peps/pep-3147/

# len(code) == 17 (both in CPython and on unix port)
def no_args():
    pass

# len(code) == 18 (CPython) and 19 (MicroPython)
def one_arg(a):
    pass

# the new cellvars code object field means the code object is now bigger:
# len(code) == 23 (CPython) and 24 (Micro
