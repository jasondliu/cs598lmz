import weakref
# Test weakref.ref(obj).__call__()

class C(object):
    def __init__(self):
        self.__dict__['x'] = 1

    def __call__(self):
        return 42

def callback(r):
    print "callback", r()

def test_callable_ref():
    c = C()
    r = weakref.ref(c, callback)
    print r()
    c.x = 2
    print r()
    del c
    gc.collect()
    print r()

test_callable_ref()

# Test weakref.ref(obj, callback)

class C(object):
    def __init__(self):
        self.__dict__['x'] = 1

    def __call__(self):
        return 42

def callback(r):
    print "callback", r()

def test_callable_ref():
    c = C()
    r = weakref.ref(c, callback)
    print r()
    c.x = 2
    print r()
    del c
   
