import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(str(),callback)
class X(object):pass
keepalive.append(X)
class B(list):
    def __init__(self):
        self.attr=[]
    def __getattr__(self,name):
        print 'getattr:',name
        return getattr(self.attr,name)
    def __setattr__(self,name,value):
        print 'setattr:',name,value
        return setattr(self.attr,name,value)
    def __delattr__(self,name):
        print 'delattr:',name
        return delattr(self.attr,name)
class C(object):
    def __getattribute__(self,name):
        print 'getattr:',name
        return object.__getattribute__(self,name)
    def __setattr__(self,name,value):
        print 'setattr:',name,value
        return object.__setattr__(self,name,value)
    def __delattr__(self
