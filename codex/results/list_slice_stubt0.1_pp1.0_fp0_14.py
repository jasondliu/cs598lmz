import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

#结果：['', <__main__.A object at 0x000002A8B9E7A898>]
#结论：弱引用不会增加对象的引用计数，但是弱引用对象的引用计数不为0，则不会被回收

#示例2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
gc.collect()
print(lst)

#
