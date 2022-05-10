fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14077: segfault when the __code__ attribute is not a code object
# but a generator.

import sys

def f():
    raise StopIteration()

def g():
    yield f

def h():
    yield g

def i():
    yield h

def j():
    yield i

def k():
    yield j

def l():
    yield k

def m():
    yield l

def n():
    yield m

def o():
    yield n

def p():
    yield o

def q():
    yield p

def r():
    yield q

def s():
    yield r

def t():
    yield s

def u():
    yield t

def v():
    yield u

def w():
    yield v

def x():
    yield w

def y():
    yield x

def z():
    yield y

def a():
    yield z

def b():
    yield a

def c():

