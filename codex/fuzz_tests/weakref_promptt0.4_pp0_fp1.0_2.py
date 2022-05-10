import weakref
# Test weakref.ref()
def f():
    return 42
o = f
wr = weakref.ref(o)
print wr(), wr() is o, wr() is f
del o
print wr()

# Test weakref.proxy()
class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<C %s>" % self.x
o = C(42)
wp = weakref.proxy(o)
print wp, wp.x
del o
try:
    print wp.x
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()
o = C(42)
wp = weakref.proxy(o)
wr = weakref.ref(o)
print weakref.getweakrefcount(o), weakref.getweakrefcount(wp), weakref.getweakrefcount(wr)

# Test weakref.getweakrefs()
l = weakref.getweakrefs(o)
print len(l), l[0] is wr
