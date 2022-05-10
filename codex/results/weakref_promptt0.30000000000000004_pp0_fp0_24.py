import weakref
# Test weakref.ref(x)
def f():
    x = weakref.ref(42)
    print(x())

f()

def f():
    x = weakref.ref(42)
    print(x())
    del x

f()

def f():
    x = weakref.ref(42)
    print(x())
    del x
    print(x())

f()

def f():
    x = weakref.ref(42)
    print(x())
    del x
    print(x())
    print(x())

f()

def f():
    x = weakref.ref(42)
    print(x())
    del x
    print(x())
    print(x())
    print(x())

f()

def f():
    x = weakref.ref(42)
    print(x())
    del x
    print(x())
    print(x())
    print(x())
    print(x())

f()

def f():
    x = weakref.ref(42)

