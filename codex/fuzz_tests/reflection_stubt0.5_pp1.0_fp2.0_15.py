fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()

# issue 5
class A:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a
    def __hash__(self):
        return hash(self.a)

class B:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a
    def __hash__(self):
        return hash(self.a)

d = {}
d[A(1)] = 1
d[B(1)] = 2
assert d[A(1)] == 2

# issue 6
def f(a, b, c):
    return a, b, c

assert f(1, *(2,)) == (1, 2, None)

# issue 7
def f(a, b, c):
    return a, b, c

assert f(*(1,), **{'b': 2}) == (1
