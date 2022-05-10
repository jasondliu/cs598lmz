from types import FunctionType
a = (x for x in [1])
# type(a)

def test():
    yield 1

type(test) == FunctionType

print(type(test))

class A(object):
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name2(self):
        return self.name

    def __call__(self):
        print('call me')

class B(A):
    pass

a = A('hello')
print(a.name2)
a()
b = B('world')
print(b.name2)
b()
