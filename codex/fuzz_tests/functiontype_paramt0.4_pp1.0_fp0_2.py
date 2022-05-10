from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test __repr__
class Foo:
    def __repr__(self):
        return 'foo'

repr(Foo())

# Test __delattr__
class Foo:
    def __delattr__(self, name):
        print(name)

f = Foo()
del f.foo

# Test __format__
class Foo:
    def __format__(self, format_spec):
        return 'foo'

format(Foo(), '')

# Test __getattribute__
class Foo:
    def __getattribute__(self, name):
        print(name)

f = Foo()
f.foo

# Test __getattr__
class Foo:
    def __getattr__(self, name):
        print(name)

f = Foo()
f.foo

# Test __hash__
class Foo:
    def __hash__(self):
        return 42

hash(Foo())

# Test __init__
class Foo:
    def __init__
