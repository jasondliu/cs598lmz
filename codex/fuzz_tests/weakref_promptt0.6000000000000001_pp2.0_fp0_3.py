import weakref
# Test weakref.ref(a, callback) returns a weak reference to a.

class Foo:
    pass

def callback(w):
    print "callback called with", w
    raise SystemExit

f = Foo()

w = weakref.ref(f, callback)
print w
del f
print w

print
print "test with class"
class Foo2:
    def __del__(self):
        print "Foo2.__del__"

def callback2(w):
    print "callback2 called with", w

f = Foo2()
w = weakref.ref(f, callback2)
print w
del f
print w
