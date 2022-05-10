import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
counter = itertools.count()
def f():
    n = next(counter)
    if n > 1000:
        return
    L = [0] * n
    f()

f()

gc.collect()

# Test gc.get_objects()
def closure():
    a = []
    def f():
        b = []
        return a, b
    return f

# Test gc.get_referrers()
class WithMethod:
    def m(self):
        return WithMethod()

class WithFinalizer:
    def __del__(self):
        pass

l = []
l.append(l)

def f():
    return WithMethod()

def g():
    return WithFinalizer()

def h():
    return WithFinalizer()

def i():
    return WithFinalizer()

def j():
    return WithMethod()

def k():
    return WithFinalizer()

def l():
    return WithFinalizer()

def m():
    return WithFinalizer()

class New
