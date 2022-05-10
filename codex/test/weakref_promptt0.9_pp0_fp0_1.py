import weakref
# Test weakref.ref enough to know it is implemented.
class Foo:
    pass

foo = Foo()
r = weakref.ref(foo)
r().__class__

class WeakKeyDictionary:
    def __init__(self):
        self.d = {}

    def __getitem__(self, object):
        oid = id(object)
        return self.d[oid]

    def __setitem__(self, object, value):
        oid = id(object)
        self.d[oid] = value


class MyBase:
    pass


class MyClass(MyBase):
    pass


class MetaWeakKeyDictionary(type):
    all_refs = WeakKeyDictionary()
    def __init__(cls, name, bases, clsdict):
        print("In MetaWeakKeyDictionary.__init__()")
        print("   cls:", cls)
        if name != "__main__.MyBase":
            print("   registering cls in all_refs")
