import weakref
# Test weakref.ref()

class C:
    pass

obj = C()
r = weakref.ref(obj)
print r() is obj

del obj
print r() is None


# Test weakref.proxy()

class C:
    def meth(self):
        return 42

obj = C()
p = weakref.proxy(obj)
print p.meth()
try:
    p.undefined
except AttributeError:
    print "AttributeError"

del obj
try:
    p.meth()
except ReferenceError:
    print "ReferenceError"


# Test weakref.ref() factory

class C:
    pass

obj = C()
r = weakref.ref(obj)
print r() is obj

del obj
print r() is None

# Test weakref.proxy() factory

class C:
    def meth(self):
        return 42

obj = C()
p = weakref.proxy(obj)
print p.meth()
try:
    p.undefined
except AttributeError:
    print "
