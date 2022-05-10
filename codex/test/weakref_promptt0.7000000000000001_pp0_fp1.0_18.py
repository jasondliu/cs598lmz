import weakref
# Test weakref.ref.__call__()
# Bug #97460

class Foo:
    def __init__(self, x):
        self.x = x

class Bar:
    def __init__(self, x):
        self.x = x

# Callable weak reference to callable object
foo = Foo(42)
x = weakref.ref(foo.__call__)()
if x != foo.x:
    raise RuntimeError('__call__() failed')

# Callable weak reference to function
bar = Bar(42)
x = weakref.ref(bar.x)()
if x != bar.x:
    raise RuntimeError('__call__() failed')
