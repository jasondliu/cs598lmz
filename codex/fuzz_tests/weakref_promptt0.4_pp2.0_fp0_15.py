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
    print r()

def g():
    c = C('g')
    r = weakref.ref(c)
    print r()

f()
g()

# Test weakref.ref(obj, callback)

def f():
    c = C('f')
    r = weakref.ref(c, lambda x: print('callback', x))
    print r()

def g():
    c = C('g')
    r = weakref.ref(c, lambda x: print('callback', x))
    print r()

f()
g()

# Test weakref.ref(obj, callback) with a class

class C(object):
    def __init__(self, name):
        self.name = name
   
