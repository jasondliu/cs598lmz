import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print(len(lst))
del keepalive
gc.collect()
print(len(lst))
lt=[1,2,3]
class A(object):
    def __init__(self):
        self.a=lt
class B(object):
    def __init__(self):
        self.a=A()
b=B()
keepalive=b.a.a
del b.a
del b
import gc
gc.collect()
print(lt)
