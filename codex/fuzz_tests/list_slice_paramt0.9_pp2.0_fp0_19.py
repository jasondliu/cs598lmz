import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c),callback)
print(gc.collect())
print(lst)
print(a.c)
del a
print([i for i in gc.get_referrers(str()) if isinstance(i,list)])

#=============================
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
#a.c=a
keepalive.append(weakref.ref(a,callback))
print(gc.collect())
print(lst)
print(a)
del a
print([i for i in gc.get_referrers(str()) if isinstance(i,list)])#打印结果是空列表

#=====================================
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
b=A()
a
