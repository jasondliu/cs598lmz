import types
types.FunctionType

class A(object):
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

a = A(1)
a(2)

type(a)
type(A)

def f():
    pass

type(f)

class B(object):
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y
    def __str__(self):
        return 'B(%s)' % self.x
    def __repr__(self):
        return 'B(%s)' % self.x

b = B(1)
