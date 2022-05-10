import gc, weakref
import sys

class C(object):
    pass

c = C()

def f():
    c.attr = 'local'

def g():
    c.attr = 'global'

def h():
    c = C()
    c.attr = 'local'

def i():
    c = C()
    c.attr = 'global'

def j():
    c = C()
    c.attr = 'local'
    def f():
        c.attr = 'nested'
    f()

def k():
    c = C()
    c.attr = 'global'
    def f():
        c.attr = 'nested'
    f()

def l():
    ref = weakref.ref(C())
    c = ref()
    c.attr = 'local'

def m():
    ref = weakref.ref(C())
    c = ref()
    c.attr = 'global'

def n():
    def f():
        c = C()
        c.attr = 'local'
    f
