import weakref
# Test weakref.ref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<C %s>" % (self.name,)

def work(obj): # can fire at any time
    print("working on", repr(obj))
    del obj


s = C("s")
w = weakref.ref(s, work)
print("  Before:", w)
gc.collect()
print("After:", w)

w = weakref.ref(s)
print("  Before:", w)
gc.collect()
print("After:", w)

w = weakref.ref(s, work)
r = weakref.ref(5)
print("  Before:", w, r)
gc.collect()
print("After:", w, r)

def test():
    class Foo:
        pass

    def callback(ref):
        print("weakly referenced object died")

    foo = Foo()
    wfoo = weakref.ref(foo, callback)
