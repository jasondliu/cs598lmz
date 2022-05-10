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

#结果：['<__main__.A object at 0x7f8c8d8e7f98>']
#结论：弱引用的对象，在没有强引用的时候，会被回收，但是回收的时候，会调用回调函数，回调函数中可以访问到弱引用的对象

#示例2：
import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

