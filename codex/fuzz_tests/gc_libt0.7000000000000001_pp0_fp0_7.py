import gc, weakref

class Foo(object):
    def __init__(self, i):
        self.i = i

def callback(r):
    print "Dead", r.i

def create(i):
    o = Foo(i)
    wr = weakref.ref(o, callback)
    return o

print gc.collect()
create(1)
print gc.collect()
o2 = create(2)
print gc.collect()
del o2
print gc.collect()
