fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__ = (1).__code__
takes_code = lambda x: type(x)(1)
takes_code(gi)


class Callable(object):
    __call__ = lambda: None

call = Callable()
call()

abs(-1)
abs(-1.0)
abs(-1j)
abs(1j)

import decimal
decimal.Decimal(1).ln()

def f(self): pass
f.__class__ = 1
f(1)

func = lambda: None
func.__class__ = 1
func()

obj = object()
obj.__class__ = 1
del obj.__class__

tup = tuple()
tup.__class__ = 1
del tup.__class__

def f(self, x): pass
f.__code__ = type("f", tuple(), {"co_argcount": -1})
f("a")
f("a", "b")

def f(self, x): pass
f.__code__ = type("f", tuple(),
