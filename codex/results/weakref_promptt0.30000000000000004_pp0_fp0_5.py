import weakref
# Test weakref.ref

class C:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "del"

c = C(1)
r = weakref.ref(c)
print r() is c
print r().x
c = None
print r() is None

# Test weakref.WeakKeyDictionary

class C:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "del"

c1 = C(1)
c2 = C(2)
d = weakref.WeakKeyDictionary()
d[c1] = 1
d[c2] = 2
print d[c1]
print d[c2]
c1 = None
print d[c2]
c2 = None
print d

# Test weakref.WeakValueDictionary

class C:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "del"


