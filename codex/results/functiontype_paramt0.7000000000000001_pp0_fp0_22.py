from types import FunctionType
list(FunctionType(lambda x: x + 1, lambda x: x * 2, lambda x: x ** 3).__init__)  # [<function <lambda> at 0x7f5e6a90b200>, <function <lambda> at 0x7f5e6a90b268>, <function <lambda> at 0x7f5e6a90b2f0>]

class Foo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __add__(self, other):
        return Foo(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other):
        return Foo(self.a - other.a, self.b
