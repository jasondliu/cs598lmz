import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用的一个应用场景是缓存
# 如果缓存的对象是强引用，那么缓存的对象永远不会被回收，缓存的对象会占用内存，如果缓存的对象是弱引用，那么缓存的对象会被回收，缓存的对象不会占用内存
# 这里演示一个缓存的例子
import weakref
class A(object):pass
def callback(x):del lst[0]
