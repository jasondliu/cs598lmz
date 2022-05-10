from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'foo'))

# Issue #17
def f():
    yield
    yield
    yield

# Issue #18
class C(object):
    def __init__(self):
        self.__dict__ = {'a': 1}

# Issue #19
class D(object):
    def __init__(self):
        self.__dict__ = {'a': 1}
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

# Issue #20
class E(object):
    def __init__(self):
        self.__dict__ = {'a': 1}
    def __getattr__(self, name):
        return object.__getattribute__(self, name)

# Issue #21
class F(object):
    def __init__(self):
        self.__dict__ = {'a': 1}
    def __getattribute__(self, name):
        if name == 'a':
            return object.__getattribute__(
