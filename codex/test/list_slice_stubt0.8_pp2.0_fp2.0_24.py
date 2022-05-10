import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=str()
a.d=weakref.ref(a,callback)
weakref.ref(a,callback)
weakref.ref(a,callback)
keepali0e.append(lst)
a.e=a.b
del a.c
del a.d
del a.b
del a.a
a.b=str()

# 内存泄漏
class A(object):
    def __init__(self):
        self.b=2
        del self.a
    def __del__(self):
        self.b=1
        del self.a
class B(object):
    def __init__(self):
        self.a=A()
    def __del__(self):
        self.a.b
