from types import FunctionType
a = (x for x in [1])


def g():
    yield 10


def g2(x: FunctionType):
    yield from x()


try:
    print(g2(a))
except TypeError:
    print("Can't send non-generator to 'yield from'.")
print(next(g2(g)))
