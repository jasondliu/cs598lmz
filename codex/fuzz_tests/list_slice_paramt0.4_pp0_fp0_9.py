import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=None
del a
del keepali0e
print lst

def f():pass
def g():pass
f.__code__=g.__code__
f()

class A(object):pass
def f():pass
a=A()
a.__class__=type(f)
a()

class A(object):
    def __init__(self,x):
        self.x=x
    def __eq__(self,other):
        return self.x==other
    def __hash__(self):
        return self.x
a=A(1)
d={a:1}
print d[a]
print d[1]

class A(object):pass
class B(object):pass
a=A()
b=B()
a.__class__=b.__class__

class A(object):
    def __init__(self,x):
        self.x=x
    def __eq__(self,other):
        return self.x==other
a=A(1)

