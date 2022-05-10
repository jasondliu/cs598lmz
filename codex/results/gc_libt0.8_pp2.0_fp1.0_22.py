import gc, weakref

class B(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

def f():
    a = A()
    b = B(a)
    c = weakref.ref(b)
    del a, b
    gc.collect()
    return c

print f()()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Foo %r>' % (self.name,)

def main():
    # create cycle
    f1 = c1 = Foo('f1')
    f2 = c2 = Foo('f2')
    f1.other = c2
    f2.other = c1

    # create weakrefs, but don't break the cycles
    w1 = weakref.ref(f1)
    w2 = weakref.ref(f2)
    print w1, w1()
    print
