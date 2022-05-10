import weakref
# Test weakref.ref on a class.
class C:
    pass

o = C()
r = weakref.ref(o)
print r()

o2 = r()
print o2 is o
print o2 == o
print type(o2)
print type(o)


# Test weakref.proxy on a class.
p = weakref.proxy(o)
print p
print p is o
print p == o
print type(p)
print type(o)

# Test weakref.proxy on a builtin.
p = weakref.proxy(sys)
print p.version
print p.version_info
print p.maxsize
print p.path
print p.builtin_module_names

# Test weakref.proxy on a function.

def f(): pass
p = weakref.proxy(f)
print p()

class D:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

d = weakref.WeakKeyDictionary()

d[
