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

#结果：['<__main__.A object at 0x0000000003A8C908>']
#结论：循环引用的对象不会被回收

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
#结论：没有循环引用的对象会被回收

#练习3：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
