import weakref
# Test weakref.ref(obj, callback)

class C:
    pass

def f(o):
    print 'callback'

def test(o):
    r = weakref.ref(o, f)
    print r()
    del o
    print r()

o = C()
test(o)

class D:
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return self.value
    def __eq__(self, other):
        return self.value == other.value

def f(o):
    print 'callback'

def test(o):
    r = weakref.ref(o, f)
    print r()
    del o
    print r()

o = D(1)
test(o)

class E:
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return self.value
    def __eq__(self, other):
        return self.value == other.value
    def __call__
