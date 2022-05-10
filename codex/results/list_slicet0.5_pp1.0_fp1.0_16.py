import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#第二种方法
import weakref,gc
class A(object):pass
def callback(x):print x
class B(object):
    def __init__(self,a):
        self.a=a
        self.wr=weakref.ref(a,callback)
    def __del__(self):
        print 'B.__del__'
def test():
    a=A()
    b=B(a)
    a.b=b
    del a
    del b
    gc.collect()

#第三种方法
import weakref,gc
class A(object):pass
def callback(x):
    print x
    print 'callback'
class B(object):
    def __init__(self,a):
        self.a=a
        self.wr=weakref.ref(a,callback)
    def __del__(self):
        print 'B.__del__'
def test():
    a=A()
    b=B(a)
    a.
