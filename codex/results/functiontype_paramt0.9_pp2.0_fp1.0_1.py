from types import FunctionType
list(FunctionType(a,b,c) for a,b,c in ((1,2,3),))

__all__ = [a, b]

x = "hi" + "hi"

def f134(s):
    return not s
f134.__doc__

d = dict((a,b) for a in [(1,2),(11,34)])

def f14():
    from a import b,c
    from a import b as c
    from a import b,c as d
    from a import b as c,d
    from a import (b,c)
    from a import (b,c as d)
    from a import (b as c,d)
    from a import (b,c) as d
    from a import (b as c,d) as d

def f15(a, b=1, *args, **kwargs):
    pass

def f16(a, b=1, *args):
    pass

def f17(a, b=1, *, c, **kwargs):
    pass

def
