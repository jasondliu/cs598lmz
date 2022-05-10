import weakref
# Test weakref.ref(x)
# Test weakref.proxy(x)
# Test weakref.getweakrefcount(x)
# Test weakref.getweakrefs(x)

class Foo: pass

# This is a non-refcounted object, but it should still work.
class Classic: pass

class Int:
    def __init__(self, value):
        self.value = value
    def __int__(self):
        return self.value

class OldStyle:
    pass

class OldStyle2(OldStyle):
    pass

class OldStyle3(OldStyle, Classic):
    pass

class Classic3(Classic, OldStyle):
    pass

class Derived(Foo):
    pass

class Derived2(Derived):
    pass

class Test:
    def __init__(self, subtype):
        self.subtype = subtype
    def __call__(self):
        return self.subtype()

def test():
    # Test weakref.ref(x)
    f = Foo()
