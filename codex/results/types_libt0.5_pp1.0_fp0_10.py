import types
types.MethodType(lambda self: None, None, Foo)

# test for issue #3928
class A:
    def __init__(self):
        self.foo = 'foo'
    def __getattribute__(self, attr):
        if attr == 'foo':
            return super().foo
        return super().__getattribute__(attr)

a = A()
a.foo

# test for issue #3929
class A:
    def __init__(self):
        self.foo = 'foo'
    def __getattribute__(self, attr):
        if attr == 'foo':
            return super().__getattribute__('foo')
        return super().__getattribute__(attr)

a = A()
a.foo

# test for issue #3930
class A:
    def __init__(self):
        self.foo = 'foo'
    def __getattribute__(self, attr):
        if attr == 'foo':
            return super().__getattribute__(attr)
        return super().__getattribute__(
