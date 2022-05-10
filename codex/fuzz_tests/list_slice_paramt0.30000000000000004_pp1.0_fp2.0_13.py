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

#结果：['<__main__.A object at 0x00000000029F6BE0>']
#结论：不会被回收

#第二种情况
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

#结果：['<__main__.A object at 0x00000000029F6BE0>']
#结论：不会被回收

#第三种情况
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str
