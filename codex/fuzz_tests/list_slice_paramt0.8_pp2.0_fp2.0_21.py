import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
del a
print collect()
l=lst[0]
print l
class A(object):
    pass
class B(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        del self.a
a=A()
b=B(a)
a.b=b
del a,b
print collect()
class A(object):
    pass
class B(object):
    pass
class C(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        del self.a
a=A()
a.b=B()
a.c=C(a)
del a
print collect()
class A(object):pass
def callback(obj):
    print obj,'deleted'
a=A()
b=A()
a.b=b
b.a=a
a.c=b
weakref.ref(a,callback)
del a
b.c=None
del b

