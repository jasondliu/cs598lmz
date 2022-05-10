import types
# Test types.FunctionType with decimal.Decimal inputs/outputs.

from types import FunctionType
from decimal import Decimal
from test import test_support
from test.test_support import verbose, original_stdout

class Base:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "Base(%s)" % self.x

    def method_of_base_class(self, p):
        return Decimal(p)

class Derived(Base):
    pass

class Derived2(Base):
    def method_of_base_class(self, p):
        return Base.method_of_base_class(self, p) + Decimal(1)

def test(a):
    a(Decimal(10))
    a(Decimal(2)/Decimal(3))
    a(Decimal('nan'))
    a(Decimal('inf'))

def test_object(a, ty1):
    class Token:
        def __init__(self, name, value):
            self
