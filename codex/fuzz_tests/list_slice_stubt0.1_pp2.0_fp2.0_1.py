import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#结果：
#[str(), <weakref at 0x000002A5E5D8B948; to 'A' at 0x000002A5E5D8B898>]
#这里的结果是因为a.c=a，所以a的引用计数为2，所以不会被回收，所以lst中的弱引用不会被回收

#示例2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.
