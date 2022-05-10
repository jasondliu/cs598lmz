from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
def g():
    yield 1
print(isinstance(g(), Iterator))
print(isinstance(a, Iterable))
print(isinstance(g(), Iterable))
print(isinstance(g(), Generator))
print(isinstance(a, Generator))
print(isinstance(g, FunctionType))
g_ = g()
print(isinstance(g_, FunctionType))
