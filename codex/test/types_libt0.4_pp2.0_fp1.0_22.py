import types
types.ClassType

class C(object):
    def __init__(self,x):
        self.x = x
    def __repr__(self):
        return 'C(%s)' % self.x

class D(C):
    def __init__(self,x):
        C.__init__(self,x)
    def __repr__(self):
        return 'D(%s)' % self.x

class E(C):
    def __init__(self,x):
        C.__init__(self,x)
    def __repr__(self):
        return 'E(%s)' % self.x

class F(D,E):
    def __init__(self,x):
        D.__init__(self,x)
        E.__init__(self,x)
    def __repr__(self):
        return 'F(%s)' % self.x

class G(F):
    def __init__(self,x):
        F.__init__(self,x)
   
