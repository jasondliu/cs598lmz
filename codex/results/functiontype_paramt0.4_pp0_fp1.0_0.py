from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# __slots__
class A:
    __slots__ = ['foo']
    def __init__(self):
        self.foo = 1

class B(A):
    __slots__ = ['bar']
    def __init__(self):
        super().__init__()
        self.bar = 2

b = B()
b.foo
b.bar

# __new__
class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, *args, **kwargs):
        pass

a = A()

# __init_subclass__
class A:
    def __init_subclass__(cls, *args, **kwargs):
        pass

class B(A):
    pass

class C(A, *args, **kwargs):
    pass

# __prepare__
class A:
    def __prepare__(self, *args, **
