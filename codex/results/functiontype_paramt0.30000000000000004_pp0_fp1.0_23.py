from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# __getitem__
class Foo:
    def __getitem__(self, index):
        return index

list(Foo())

# __iter__
class Foo:
    def __iter__(self):
        yield 1
        yield 2

list(Foo())

# __getattr__
class Foo:
    def __getattr__(self, name):
        if name == 'bar':
            return 1
        raise AttributeError(name)

list(Foo())

# __getattribute__
class Foo:
    def __getattribute__(self, name):
        if name == 'bar':
            return 1
        raise AttributeError(name)

list(Foo())

# __call__
class Foo:
    def __call__(self):
        yield 1
        yield 2

list(Foo())

# __len__
class Foo:
    def __len__(self):
        return 2

list(Foo())

# __contains__
class
