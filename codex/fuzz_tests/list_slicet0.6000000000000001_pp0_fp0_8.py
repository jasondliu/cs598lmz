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
print keepali0e
#下面的代码可以模拟gc.collect()
import gc,weakref
class A(object):pass
def callback(x):pass
a=A()
b=A()
a.c=b
b.c=a
keepali0e=weakref.ref(a,callback)
del a
del b
gc.collect()

#del和垃圾回收
import gc
class A(object):pass
def callback(x):
    print "callback",x
a=A()
callback(a)
keepali0e=weakref.ref(a,callback)
callback(a)
del a
callback(a)
gc.collect()
callback(a)
#下面的代码模拟了A的实例被回收
import weakref
class A(object):pass
a=A()
b=A()
a.c=b
b.
