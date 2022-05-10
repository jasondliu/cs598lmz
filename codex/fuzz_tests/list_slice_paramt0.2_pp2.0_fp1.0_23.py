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

#结果：['<__main__.A object at 0x00000000029A7E10>']
#结论：当对象a被删除后，a.c依然存在，所以a不会被回收

#示例2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del a.c
print lst

#结果：[]
#结论：当对象a被删除后，a.c依然存在，所
