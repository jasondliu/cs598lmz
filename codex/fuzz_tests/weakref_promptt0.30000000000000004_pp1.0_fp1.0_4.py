import weakref
# Test weakref.ref(self)
class C(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "del", self.x
    def __repr__(self):
        return "<C %s>" % self.x

class D(C):
    def __init__(self, x):
        C.__init__(self, x)
        self.wr = weakref.ref(self)
    def __del__(self):
        print "del D", self.x

class E(C):
    def __init__(self, x):
        C.__init__(self, x)
        self.wr = weakref.ref(self)
    def __del__(self):
        print "del E", self.x

class F(C):
    def __init__(self, x):
        C.__init__(self, x)
        self.wr = weakref.ref(self)
    def __del__(self):
        print "del F", self.x


