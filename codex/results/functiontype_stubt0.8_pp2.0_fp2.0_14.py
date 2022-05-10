from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator), isinstance(a, Iterable), isinstance(a, Generator), isinstance(a, FunctionType))
# True True True False

def f():
    yield 1

print(isinstance(f, FunctionType), isinstance(f(), Generator))
# True True

b = (1)
print(isinstance(b, Iterator), isinstance(b, Iterable), isinstance(b, Generator), isinstance(b, FunctionType))
# False False False False

c = (1 for i in range(1))
print(isinstance(c, Iterator), isinstance(c, Iterable), isinstance(c, Generator), isinstance(c, FunctionType))
# True True True False

d = [1]
print(isinstance(d, Iterator), isinstance(d, Iterable), isinstance(d, Generator), isinstance(d, FunctionType))
# False True False False


e = []
print(isinstance(e, Iterator), isinstance(e, Iterable), isinstance(e, Generator), isinstance(e,
