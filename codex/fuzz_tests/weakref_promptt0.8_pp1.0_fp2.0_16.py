import weakref
# Test weakref.ref with weakref.getweakrefcount returning >0 for a list.
import _weakref

class MyList(list):
    pass

l = MyList()
wr = _weakref.ref(l)
l.append(l)
l.append(l)
l.append(l)
#print _weakref.getweakrefcount(l)
#del l
assert repr(wr()) == "MyList([MyList(...), MyList(...), MyList(...)])"

# Test weakref.ref with a dict-like object.

class MyDict:
    def __init__(self):
        self.d = {1: "hello", 2: "world"}

    def __eq__(self, other):
        return self.d == other.d

    def __hash__(self):
        return id(self.d)

    def __repr__(self):
        return "MyDict(%s)" % repr(self.d)

d = MyDict()
wr = _weakref.ref(d)
del d
assert wr
