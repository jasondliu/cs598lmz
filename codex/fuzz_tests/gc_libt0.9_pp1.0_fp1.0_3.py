import gc, weakref


class Impl(object):
    def __init__(self, source):
        self.source = source
        self.data = []
        self.rref = weakref.ref(self, self.clean)
    def append(self, value):
        self.data.append(value)
        self.rref = weakref.ref(self, self.clean)
    def clean(self, ph):
        print "cleaning up %s %s" % (ph, self.source)
        self.source = None
        self.data = None
    
    
def create_impl(source):
    obj = Impl(source)
    #return weakref.proxy(obj)
    return obj
    
    
def use(obj_proxy):
    print repr(obj_proxy)
    return obj_proxy
    
    
def test_weak_proxy():
    a = create_impl("A")
    ap = weakref.proxy(a)
    
    use(ap)
    
    a.append("A1")
    use(ap)
    
    a
