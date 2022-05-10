import weakref
# Test weakref.ref()
import operator


class C:
    pass

o = C()
r = weakref.ref(o)
print type(r)
print o is r()
r2 = weakref.ref(o)
print r is r2

class MyObject:
    def myMethod(self):
        pass

o = MyObject()
r = weakref.ref(o)
print r().myMethod

# Test callback registration
objs = []
def remove(ref):
    objs.remove(ref)

for i in range(10):
    o = C()
    r = weakref.ref(o, remove)
    objs.append(r)

del o
for o in objs:
    o()

print objs
del o

# Test callback
calls = []
def remove(ref):
    calls.append(ref)

o = C()
r = weakref.ref(o, remove)
del o
print calls

# Test WeakKeyDictionary
w = weakref.WeakKeyDictionary()
o = C()
