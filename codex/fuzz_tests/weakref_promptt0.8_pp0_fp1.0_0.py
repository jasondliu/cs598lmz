import weakref
# Test weakref.ref
class C:
    pass
a = C()
b = weakref.ref(a)
print a
print b
print b()

# Test weakref.proxy
class C:
    def __init__(self, x=1):
        self.x = x
    def getx(self):
        return self.x
    def setx(self, x):
        self.x = x
    def delx(self):
        del self.x
    x = property(getx, setx, delx)
a = C()
b = weakref.proxy(a)
print a.x
print b.x
b.x = 2
print a.x
print b.x
try:
    del b.x
except AttributeError:
    print "AttributeError: x"
print a.x

# Test weakref.ref(None)
try:
    weakref.ref(None)
except TypeError:
    print "TypeError"

# Test deallocation of the last proxy
class C:
    pass
a = [C()]

