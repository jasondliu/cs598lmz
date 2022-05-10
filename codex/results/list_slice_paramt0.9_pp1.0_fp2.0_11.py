import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='a'
del a
del lst
print(keepali0e[0]())
class C(dict):
    def __init__(self,a=1,**kw):
        super().__init__(**kw)
        self.a=self.get(a,a)
