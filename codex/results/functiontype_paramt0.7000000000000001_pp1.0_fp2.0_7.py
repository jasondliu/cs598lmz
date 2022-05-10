from types import FunctionType
list(FunctionType(a).__closure__)

a = '''def f(x):
    y = x + 1
    def g(z):
        return z + y + 10
    return g'''

a = '''def make_adder_of(n):
    def adder(k):
        return k + n
    return adder'''

import dis
dis.dis(a)
a = '''def f():
    def g(x):
        return x*2
    return g
f()(5)'''

def ho(f):
    def inner(*args, **kw):
        return f(*args, **kw)
    return inner

@ho
def foo(a, b=5):
    return a + b

foo(5, b=6)

a = '''def f(x):
    def g(y):
        return x + y
    return g

f(1)(2)'''

a = '''def f():
    x = 5
    def g():
        nonlocal x
        x += 1
       
