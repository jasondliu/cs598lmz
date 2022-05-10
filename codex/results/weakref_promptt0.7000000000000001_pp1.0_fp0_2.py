import weakref
# Test weakref.ref with a callback

class Foo:
    pass

def callback(r, list_r):
    print 'callback:', r
    list_r.append(r)

list_wr = []

f = Foo()
wr = weakref.ref(f, callback, list_wr)

del f
import gc; gc.collect()
print 'list_wr:', list_wr

assert len(list_wr) == 1
assert list_wr[0]() is None
# Test weakref.ref for objects with a custom __hash__

class Foo:
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return self.value

list_wr1 = []
list_wr2 = []
list_wr3 = []

f1 = Foo(1)
f2 = Foo(2)
f3 = Foo(3)
f4 = Foo(4)

wr1 = weakref.ref(f1, callback, list_wr1)
wr2 = weakref.ref(f2
