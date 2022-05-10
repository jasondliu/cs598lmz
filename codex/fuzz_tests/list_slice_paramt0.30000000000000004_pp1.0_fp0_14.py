import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

#__slots__
class A(object):__slots__=['a','b']
a=A()
a.a=1
a.b=2
a.c=3

#__getattr__
class A(object):
    def __getattr__(self,name):
        if name=='c':
            return 3
        else:
            raise AttributeError(name)
a=A()
a.c

#__getattribute__
class A(object):
    def __getattribute__(self,name):
        if name=='c':
            return 3
        else:
            return object.__getattribute__(self,name)
a=A()
a.c

#__setattr__
class A(object):
    def __setattr__(self,name,value):
        if name=='c':
            raise AttributeError(name)
        else:
            object.__setattr__(self,name,value)
a=A()
a.c=
