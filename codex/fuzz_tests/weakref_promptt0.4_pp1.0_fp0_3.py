import weakref
# Test weakref.ref()
class Foo:
    def __init__(self):
        self.x = 42
        self.ref = weakref.ref(self)
    def __repr__(self):
        return "<Foo %s>" % self.x
    def __del__(self):
        print("Foo.__del__")

def test_weakref():
    a = Foo()
    print(a)
    print(a.ref())
    del a
    print(a.ref())

# Test weakref.WeakKeyDictionary()
class Foo2:
    def __init__(self):
        self.x = 42
        self.ref = weakref.WeakKeyDictionary()
    def __repr__(self):
        return "<Foo2 %s>" % self.x
    def __del__(self):
        print("Foo2.__del__")

def test_weakref_weakkeydict():
    a = Foo2()
    print(a)
    print(a.ref)
    a.ref[a] = "hello"

