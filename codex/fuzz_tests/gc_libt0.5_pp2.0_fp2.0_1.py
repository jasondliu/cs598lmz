import gc, weakref

class A(object):
    pass

class B(object):
    pass

def check_gc(obj, name):
    print("Checking %s" % name)
    ref = weakref.ref(obj)
    print("  before gc:", ref)
    gc.collect()
    print("  after gc:", ref)

a = A()
b = B()

a.b = b
b.a = a

check_gc(a, "a")
check_gc(b, "b")

del a
del b

gc.collect()

class C(object):
    def __init__(self, value):
        self.value = value

def get_c(value):
    return C(value)

c = get_c(1)
d = get_c(2)

c.d = d
d.c = c

check_gc(c, "c")
check_gc(d, "d")

del c
del d

gc.collect()
