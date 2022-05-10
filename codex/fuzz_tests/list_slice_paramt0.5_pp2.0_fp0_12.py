import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print lst

class A(object):
    def __init__(self):
        self.b=B(self)
    def __del__(self):
        print 'del A'
class B(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        print 'del B'
a=A()
a=None

class Foo(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Foo object(name:%s)'%self.name
    def __call__(self,*args,**kwargs):
        print 'My name is %s'%self.name
f=Foo('Alex')
print f
f()

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self
