from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'f')(2))

class C(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

c = C(2)
list(c())

def f():
    yield 1
    yield 2

g = f()
list(g)

class C(object):
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self
    def next(self):
        if self.x == 0:
            raise StopIteration
        self.x -= 1
        return self.x

c = C(2)
list(c)

class C(object):
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return iter([self.x])

c = C(2)
list(c)

class C(object):
    def __init__(self, x):
       
