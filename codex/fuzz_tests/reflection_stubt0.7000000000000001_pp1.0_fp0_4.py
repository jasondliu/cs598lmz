fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Check that we can set sys.excepthook
import sys
sys.excepthook = lambda *args: None

# Check that we can call builtins.dir
dir(1)

# Check we can get/set __name__ on a function
def f(): pass
f.__name__ = "f"
f.__name__

# Check we can get/set __module__ on a function
f.__module__ = "m"
f.__module__

# Check we can get/set __qualname__ on a function
f.__qualname__ = "q.f"
f.__qualname__

# Check we can get/set __class__ on a function
f.__class__ = int

# Check we can get/set __annotations__ on a function
f.__annotations__ = {'a': 1}
f.__annotations__

# Check we can get/set __kwdefaults__ on a function
def g(a, b=1, *, c=2, d, **kws): pass

