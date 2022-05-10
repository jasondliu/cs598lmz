from types import FunctionType
list(FunctionType('foo', globals(), None, None, None, 42))

# __length_hint__
class Foo:
    def __length_hint__(self):
        return 5

len(Foo())

# __round__
round(1.5)

# __index__
class Foo:
    def __index__(self):
        return 5

format(5, 'b')

# __getattr__
class Foo:
    def __getattr__(self, name):
        return 5
foo = Foo()
foo.bar

# __dir__
class Foo:
    def __dir__(self):
        return ['a', 'b']
dir(Foo())

# __enter__
class Foo:
    def __enter__(self):
        return 5
with Foo() as foo:
    foo

# __exit__
class Foo:
    def __exit__(self, *args):
        pass
with Foo():
    pass

# __sizeof__
class Foo:
    def __sizeof__(self):
        return 5

