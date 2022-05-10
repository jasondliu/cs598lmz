from types import FunctionType
a = (x for x in [1])
type(a)
def foo():
    yield 1
type(foo)
type(foo())
type(a)
next(foo())
next(a)
class X:
    def __init__(self):
        self.a = 1
    def haha(self):
        pass
X()
x = X()
x.a
x.haha()
z = X()
z.a = 3
z.a
x.a
y = x
y.a = 2
y.a
x.a
x.a = 3
x.a
y.a
x
y
x is y
x == y
id(x)
id(y)
w = X()
w.a = 3
x.a = 1
x.a
y.a
y is x
y == x
w.a
y is x
y == x
y.a
y.a = 2
y.a
x.a
w.a
x.a = 3
x.a
y.a
x.a
w.a
w.a = 1

