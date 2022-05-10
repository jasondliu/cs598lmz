import weakref
# Test weakref.ref
try:
    class A:
        pass
    a = A()
    a.attr = 12
    r = weakref.ref(a)
    print r().attr
except Exception, e:
    print e
try:
    r().attr = 42
    print r().attr
except Exception, e:
    print e

# Test weakref.proxy
try:
    p = weakref.proxy(a)
    print p.attr
except Exception, e:
    print e
try:
    p.attr = 42
    print p.attr
except Exception, e:
    print e

# Test weakref.ref with callbacks
name = 'fred'
lst = []
class C:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return self.n
def callit(ref):
    lst.append(ref)
    return 'unref'
def callit2(ref):
    lst.append(ref)
    return name
r3 = weakref.ref(name,
