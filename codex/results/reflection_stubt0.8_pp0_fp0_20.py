fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

class A:
    def __init__(self, f):
        self.f = f
    def __call__(self):
        return self.f()
f = lambda: 42
a = A(f)
a()

def f():
    pass
def g(a):
    a = 0
    return a
a = 1
g(a)
a

def f():
    return 2
def g(a):
    a = 0
    return a
a = 1
g(a)
a

def f():
    return True
def g(a):
    a = False
    return a
a = True
g(a)
a

def f(a):
    return a
def g(a):
    a = 1, 2
    return a
a = 0
g(a)
a

def f(a):
    return a
def g(a):
    a = a, 0
    return a
a = 0
g(a)
a

def f(a):
   
