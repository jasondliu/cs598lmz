import weakref
# Test weakref.ref(obj, callback)

class Foo:
    pass

def callback(ref):
    print("callback(", ref, ")")

def test(a):
    obj = Foo()
    print("a =", a)
    print("obj =", obj)
    r = weakref.ref(obj, callback)
    print("r =", r)
    print("r() =", r())
    print("obj =", obj)
    print("obj == r() is", obj == r())
    print("obj is r() is", obj is r())
    print("del obj")
    del obj
    print("r() =", r())
    print("gc.collect()")
    gc.collect()

test("test(a)")
test("test(b)")
test("test(c)")
