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

