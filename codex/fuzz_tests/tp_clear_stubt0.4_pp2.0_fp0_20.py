import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

# ____________________________________________________________

class C(object):
    def __del__(self):
        print "C.__del__"

def f():
    raise ValueError

def g():
    raise TypeError

def h():
    raise IndexError

def test_finally_in_destructor():
    try:
        try:
            try:
                C()
                f()
            finally:
                g()
        finally:
            h()
    except Exception, e:
        print e.__class__.__name__

test_finally_in_destructor()

# ____________________________________________________________

class Del(object):
    def __del__(self):
        print "Del.__del__"

def test_del_in_generator():
    def f():
        try:
            yield Del()
        except:
            pass
    g = f()
    g.next()
    g.throw(ValueError)

test_del_in_generator()

# ____________________________________________________________

