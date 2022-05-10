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
#['', <weakref at 0x000002A3F6D8E948; to 'A' at 0x000002A3F6D8E898>]
#这里的结果是因为a.c=a，所以a的引用计数为2，所以不会被回收，所以lst[1]不会被回收

#练习2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))

