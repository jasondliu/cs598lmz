import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
print r
o2 = r()
assert o is o2

class MyRef(weakref.ref):
    def __init__(self, ob):
        self.x = 1
        weakref.ref.__init__(self, ob)

o = C()
r = MyRef(o)
print r
print r.x
o2 = r()
assert o is o2

# get a reference to a function
def f():
    pass
r = weakref.ref(f)
assert r() is f

# get a reference to a built-in function
import sys
r = weakref.ref(len)
assert r() is len

# get a reference to a built-in method
r = weakref.ref(''.replace)
assert r() == ''.replace

# get a reference to a method
class C:
    def f(self):
        pass
o = C()
r = weakref.ref(o.f)
assert r()
