import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return "Foo(%r)" % self.arg

def callback(r):
    print("callback", r())

def test_ref():
    print("test_ref")
    f = Foo(42)
    r = weakref.ref(f, callback)
    print("r", r)
    print("f", f)
    print("r()", r())
    print("f is r()", f is r())
    print("f == r()", f == r())
    print("f is r", f is r)
    print("f == r", f == r)
    print("f is r()", f is r())
    print("f == r()", f == r())
    print("f()", f())
    print("f() is r()", f() is r())
    print("f() == r()", f() == r())
    print("f() is r", f() is r)
   
