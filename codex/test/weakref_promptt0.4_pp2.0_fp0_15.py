import weakref
# Test weakref.ref(obj)

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f():
    c = C('f')
    r = weakref.ref(c)
