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
print lst
print keepalive

#[str(), <weakref at 0x7f8c8c0a9d88; to 'A' at 0x7f8c8c0a9c50>]
#[<__main__.A object at 0x7f8c8c0a9c50>]

#第一个str()是因为lst[0]被删除了，所以lst[0]变成了str()
#第二个是因为a.c=a，所以a的引用计数为2，所以a不会被回收

#第二个例子
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive
