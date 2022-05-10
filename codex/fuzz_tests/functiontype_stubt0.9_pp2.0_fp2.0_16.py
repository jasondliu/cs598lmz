from types import FunctionType
a = (x for x in [1])
gt = FunctionType.__globals__
globals()
globals()['a']
globals().update({'a':1})
globals()['a']
globals()
a
a is [1]
var = [1]
a is var
a.next()
a.next()

def foo(n=0xFF, *b, **c):
    global d, e
    d = b
    e = c

a = ['a']
foo(0xFF, *a, **{'b':123})
d
e

def f():print 1

f = lambda: print 1
f()

a = {'a':1, 'b':2}
b = a.items()
c = a.keys()
d = a.values()
a.clear()
a
b
c
d
a = {'a':1, 'b':2}
e = a.copy()
e
import sys
sys.version
import random
random.choice([1, 2])
import os
os.curd
