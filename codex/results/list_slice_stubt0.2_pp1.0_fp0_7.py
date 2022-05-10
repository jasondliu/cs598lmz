import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(lst[0],callback)
del a
del keepalive[0]
print(lst)

#结果：['<__main__.A object at 0x000002A9C7E8C898>']
#结论：弱引用的回调函数不会被调用，因为弱引用的对象被删除后，弱引用对象也会被删除，因此不会调用回调函数。

#示例2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()

