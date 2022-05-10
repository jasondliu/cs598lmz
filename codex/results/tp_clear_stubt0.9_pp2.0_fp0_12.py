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
tb = None

def func():
    global tb
    tb = sys.exc_info()[2]
    raise NotImplementedError()

def tostring(obj):
    return ascii(obj)

def doit():
    try:
        len(LateFin())
    except NotImplementedError:
        pass

doit()


def check_free_list():
    check_null = c_void_p()
    c = 0
    t = 0
    for i in xrange(100000):
        if not gc.collect(): break
        for obj in gc.get_objects():
            if type(obj) is tuple and len(obj) == 2:
                if isinstance(obj[0], str):
                    c += 1
                    if obj[0] == 'import':
                        t += 1
                if obj[0].__class__ is tuple:
                    assert not (obj[1] - check_null)
                check_null = c_void_p(obj[1])
    assert c > 0
   
