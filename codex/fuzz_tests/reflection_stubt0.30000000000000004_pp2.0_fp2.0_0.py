fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# issue #10
class A(object):
    def __init__(self, a):
        self.a = a

def f(a):
    return A(a)

f(1)

# issue #11
def f(a):
    return a

f(1)

# issue #12
def f(a):
    return a

f(1)

# issue #13
def f(a):
    return a

f(1)

# issue #14
def f(a):
    return a

f(1)

# issue #15
def f(a):
    return a

f(1)

# issue #16
def f(a):
    return a

f(1)

# issue #17
def f(a):
    return a

f(1)

# issue #18
def f(a):
    return a

f(1)

# issue #19
def f(a):
    return a

f(
