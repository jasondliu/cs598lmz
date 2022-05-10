import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.o=str()
a.e=str()
a.d=a
a.a=a
keepali0e.append(weakref.proxy(a))
lst.append(a)
keepali0e.append(weakref.proxy(a))
del a
del lst[0]
del keepali0e[0]


#定义类
class circularref:
    def __init__(self):
        self.objs=[]
    def createobjs(self,x):
        for i in range(x):
            obj=circularref.myobjs()
            obj.x=self
            self.objs.append(obj)
    def removeobjs(self):
        for obj in self.objs:
            del obj.x
        self.objs=[]
    def __del__(self):
        pass
    class myobjs:
        x=None
        def __del__(self):
            pass

lst1=circularref()
lst2=circularref()
