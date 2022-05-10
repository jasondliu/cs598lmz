from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# __getitem__
class C:
    def __getitem__(self, i):
        return i

list(C())

# __iter__
class C:
    def __iter__(self):
        yield 1
        yield 2
        yield 3

list(C())

# __getattr__
class C:
    def __getattr__(self, name):
        if name == '__iter__':
            return lambda: iter([1, 2, 3])
        raise AttributeError(name)

list(C())

# __getattribute__
class C:
    def __getattribute__(self, name):
        if name == '__iter__':
            return lambda: iter([1, 2, 3])
        raise AttributeError(name)

list(C())

# __getattribute__ with __getattr__
class C:
    def __getattribute__(self, name):
        if name == '__iter__':
            return lambda: iter([1, 2, 3])

