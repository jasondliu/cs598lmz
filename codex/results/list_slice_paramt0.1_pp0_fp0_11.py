import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果是：['\x00']
#因为a.c=a，所以a对象的引用计数为2，所以不会被回收，所以lst中的元素不会被回收

#练习2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果是：['\x00']
#因为a.c=a，所以a对象的引用计数为2，所
