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

#结果：['<__main__.A object at 0x7f8b9c0f7b90>']
#结论：弱引用的对象在没有强引用的时候，会被回收，但是如果有循环引用的话，就不会被回收

#练习2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：[]
#结论：弱引用的对
