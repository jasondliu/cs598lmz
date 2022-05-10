import types
# Test types.FunctionType and types.LambdaType

def f():
    pass

def g(x,y):
    return x+y

def h(x,y,z=1,*n,**m):
    pass

def p(x,y,z=1,*n,u,v,**m):
    pass

def q(x,y,z=1,*n,u,v,**m):
    pass

def r(x,y,z=1,*n,u,v,**m):
    pass

def s(x,y,z=1,*n,u,v,**m):
    pass

class C:
    def __init__(self,a):
        self.a = a
    def meth(self):
        pass

class D:
    def __init__(self,a):
        self.a = a
    def meth(self,x,y,z=1,*n,**m):
        pass

class E:
    def __init__(self,a):
        self
