fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #1522
class C(object):
    def __init__(self):
        self.__dict__ = {}

# Issue #1523
class A(object):
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super(B, self).__init__(x)
        self.y = y

# Issue #1524
def f(x):
    return x

def g(x):
    return x

f(g(1))

# Issue #1525
def f(x):
    return x

def g(x):
    return x

g(f(1))

# Issue #1526
def f(x):
    return x

def g(x):
    return x

f(g(1))

# Issue #1527
def f(x):
    return x

def g(x):
    return x

g(f(1))

#
