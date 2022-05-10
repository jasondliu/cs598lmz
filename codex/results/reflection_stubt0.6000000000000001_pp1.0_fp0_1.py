fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #9291: check when a generator g has no __name__ or __qualname__
def f():
    g = (i for i in ())
    g.__name__ = 'foo'
    g.__qualname__ = 'bar'
    print(str(g))
f()

# Issue #22963: check that some builtins have __qualname__
import types
for name in ('input', 'print', 'super', 'zip'):
    b = getattr(builtins, name)
    if isinstance(b, types.BuiltinFunctionType):
        print(b.__qualname__)
