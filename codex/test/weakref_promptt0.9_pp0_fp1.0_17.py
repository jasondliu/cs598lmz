import weakref
# Test weakref.ref
def f(a):
    print("f", a)
r = weakref.ref(f, None)
if hasattr(weakref, "getweakrefcount"):
    print("weakref count for f: ", weakref.getweakrefcount(f))
else:
    print("weakref.getweakrefcount() is not supported")
print("f is ", r())
del f
print("f is", r())
# Test weakref.WeakKeyDictionary
class Foo:
    def __init__(self):
        self.d = weakref.WeakKeyDictionary()
    def remember(self, obj):
        self.d[obj] = 1
    def is_remembered(self, obj):
        return obj in self.d
foo = Foo()
# Circular reference
bar = []
foo.remember(bar)
bar.append(foo)
print("foo.is_remembered(bar): ", foo.is_remembered(bar))
del foo, bar
class Foo:
    def __init__(self):
        self.d = weakref
