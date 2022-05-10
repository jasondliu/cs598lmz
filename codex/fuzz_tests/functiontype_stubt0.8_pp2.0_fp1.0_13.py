from types import FunctionType
a = (x for x in [1])
a.__next__()

class A(object):
    def __init__(self, a: int) -> None:
        self.a = a

    @classmethod
    def func(cls):
        return cls.__name__

a = A(1)
a.func()

class B(A):
    pass

b = B(1)
b.func()

def func(a: int) -> int:
    return a

func(1)
func('a')


def func(a: int, b) -> int:
  return a

func(1,2)
"""

test_data = [
    (
        """
from types import FunctionType

class A(object):
    def __init__(self, a: int) -> None:
        self.a = a

    @classmethod
    def func(cls):
        return cls.__name__

a = A(1)
a.func()

class B(A):
    pass

b = B(1)
b.
