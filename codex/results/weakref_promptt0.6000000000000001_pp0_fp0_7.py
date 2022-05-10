import weakref
# Test weakref.ref(C())
class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name
    def __del__(self):
        print '__del__', self

# Test weakref.ref(C())
class D(C):
    def __init__(self, name):
        C.__init__(self, name)
    def __repr__(self):
        return 'D(%s)' % self.name
    def __del__(self):
        print '__del__', self

# Test weakref.ref(C())
class E(C):
    def __init__(self, name):
        C.__init__(self, name)
    def __repr__(self):
        return 'E(%s)' % self.name
    def __del__(self):
        print '__del__', self

# Test weakref.ref(C())
class F(C):
    def __init__(self, name
