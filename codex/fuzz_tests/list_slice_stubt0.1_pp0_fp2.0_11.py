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

#结果：
#['', <__main__.A object at 0x000002A9D7F9F908>]
#这里的结果是因为a.c=a，所以a对象的引用计数为2，所以不会被回收，所以lst中的a对象也不会被回收

#第二个例子：
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a

