import weakref
# Test weakref.ref() on objects that have a __del__ method

class C:
    def __del__(self):
        print("deleting", self)

def callback(reference):
    print("callback", reference)

def f():
    print("creating object")
    o = C()
    print("creating reference")
    r = weakref.ref(o, callback)

def g():
    print("creating object")
    o = C()
    print("creating reference")
    r = weakref.ref(o, callback)
    print("deleting reference")
    del r
    print("deleting object")
    del o

def h():
    print("creating object")
    o = C()
    print("creating reference")
    r = weakref.ref(o, callback)
    print("creating cycle")
    o.cycle = o
    print("deleting object")
    del o

def i():
    print("creating object")
    o = C()
    print("creating reference")
    r = weak
