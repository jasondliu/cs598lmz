fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi.gi_code)()
fn()

 
# The following is based on a test for regrtest.py.

class Spam:
    def __init__(self, *args):
        self.args = args
        self.a = "spam"

    def __repr__(self):
        return "<spam %r>" % (self.args,)

class Eggs:
    def __init__(self, x):
        self.x = x
        self.a = "eggs"

    def __repr__(self):
        return "<eggs %r>" % (self.x,)

def f(*spam):
    for i in spam:
        print(i.a)
    x, y, z = spam
    print(x.a, y.a, z.a)
    x, y = spam
    print(x.a, y.a)
    x, = spam
    print(x.a)

f(Spam(1), Eggs(2), Spam(3))
f(Eggs(4
