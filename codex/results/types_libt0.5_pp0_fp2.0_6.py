import types
types.MethodType(lambda self, x: x, None, Foo)

# https://bugs.python.org/issue37605
class Foo:
    def __init__(self):
        self.x = types.MethodType(lambda self, x: x, self)

Foo().x(42)

# https://bugs.python.org/issue37605
def foo(x):
    return types.MethodType(lambda self, x: x, None)

foo(42)
