fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi
_hasattr_ = hasattr
try:
    import __pypy__
except ImportError:
    __pypy__ = None

# ___________________________________________________________________________
# Code objects

CO_OPTIMIZED = 0x0001
CO_NEWLOCALS = 0x0002
CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008
CO_NESTED = 0x0010
CO_GENERATOR = 0x0020
CO_NOFREE = 0x0040
CO_GENERATOR_ALLOWED = 0
CO_FUTURE_DIVISION = 0x2000
CO_FUTURE_ABSOLUTE_IMPORT = 0x4000 # do absolute imports by default
CO_FUTURE_WITH_STATEMENT = 0x8000

_CELL_FLAG = 1

class Code:
    """Code objects are used by the implementation to represent a
    compiled function or a method.  Not for public consumption """

    def __init__(self, co, names, varnames, filename, name,
