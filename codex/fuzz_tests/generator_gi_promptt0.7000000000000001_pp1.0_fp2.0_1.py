gi = (i for i in ())
# Test gi.gi_code.co_firstlineno


def gf():
    yield  # not valid, but it's what we're testing here
    yield
    return


gf.gi_code.co_firstlineno
# Test gi.gi_frame.f_globals
gf.gi_frame.f_globals['__name__']
# Test gi.gi_frame.f_globals['__builtins__']
type(gf.gi_frame.f_globals['__builtins__'])
# Test gi.gi_frame.f_globals['__builtins__']['int']
import sys

sys.getrefcount(tuple)


class C:
    def __del__(self):
        pass


C.__del__.__code__
C.__del__.__code__.co_argcount

print(C.__del__.__code__.co_varnames)
print(C.__del__.__code__.co_freevars)
print(C.__del__.__
