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
print lst

lst=[]
for i in range(1000):
    a=A()
    a.c=a
    lst.append(weakref.ref(a,callback))
    a.c=None
    del a
print lst

#__getattr__
class Getattr(object):
    def __init__(self):
        self.attr=9
    def __getattr__(self,name):
        print 'getattr:',name
        return getattr(self.attr,name)
    def __setattr__(self,name,value):
        print 'setattr:',name,value
        if name=='attr':
            object.__setattr__(self,name,value)
        else:
            setattr(self.attr,name,value)

g=Getattr()
g.append(3)

#__getattribute__
class Getattribute(object):
    def __init__(self):
        self.attr=9
    def __getattribute__(
