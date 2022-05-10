import weakref
# Test weakref.ref callable
def f(x): print x
c = C()
r = weakref.ref(c, f)
del c


# Test weakref.proxy callable
class D(object):
    def __init__(self):
        self.c = C()

    def __del__(self):
        f(self.c)
d = D()
del d


# Test weakref.proxy callable for classic class
class E:
    def __init__(self):
        self.c = C()
    def __del__(self):
        f(self.c)
e = E()
del e


try:
    print weakref.getweakrefcount(42)
except TypeError:
    pass
else:
    raise Exception, "expected TypeError"

try:
    print weakref.getweakrefs(42)
except TypeError:
    pass
else:
    raise Exception, "expected TypeError"


# test classic class weakref with callbacks
class F:
    def g(self, o):
        pass
f = F()
