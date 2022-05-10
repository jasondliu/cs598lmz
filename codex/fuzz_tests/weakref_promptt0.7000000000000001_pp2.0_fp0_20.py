import weakref
# Test weakref.ref(foo) if foo is a weakrefable object.

class Foo:
    pass

class FooSub(Foo):
    pass

class FooSubSub(FooSub):
    pass

# Temporary testing objects.
def func():
    pass

class Class:
    def method(self):
        pass

class Inst(Class):
    def method(self):
        pass

class ClsSub(Class):
    pass

class InstSub(Inst):
    pass

def meth(self):
    pass

class C:
    pass

def test():
    f = Foo()
    # Can create a weakref to objects of a built-in type
    r = weakref.ref(f)
    # Can create a weakref to objects of a new-style class
    r = weakref.ref(Foo())
    r = weakref.ref(FooSub())
    r = weakref.ref(FooSubSub())
    # Can create a weakref to objects of an old-style class
    r = weakref.ref(Class())
   
