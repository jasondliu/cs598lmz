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

#结果：['', <weakref at 0x000002A0E8F9D948; to 'A' at 0x000002A0E8F9D898>]
#结论：当对象被回收时，会调用回调函数，并将弱引用从列表中删除

#示例2
import weakref
class A(object):pass
def callback(x):print('callback')
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#结果：
