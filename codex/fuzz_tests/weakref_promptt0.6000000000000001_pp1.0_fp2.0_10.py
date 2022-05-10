import weakref
# Test weakref.ref class.
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print o, r(), r() is o

del o
print gc.collect()
print r()

print repr(r)

class D:
    pass

o = D()
p = weakref.proxy(o)

print o, p, p is o

del o
print gc.collect()

try:
    print p
except ReferenceError:
    print "ReferenceError"

try:
    p.foo
except ReferenceError:
    print "ReferenceError"

try:
    p.foo = 12
except ReferenceError:
    print "ReferenceError"

try:
    del p.foo
except ReferenceError:
    print "ReferenceError"

# Test weakref.ref subclass.
class E:
    pass

class F(weakref.ref):
    def __init__(self, ob):
        self.d = {}
    def __call__(self):
        return 42

o
