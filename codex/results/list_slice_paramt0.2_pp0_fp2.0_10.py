import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print(lst)

#结果：['<__main__.A object at 0x000002A8E8F2D2E8>']
#结论：当一个对象的弱引用计数为0时，该对象会被回收，但是该对象的弱引用对象不会被回收，因为它的弱引用计数不为0

#示例2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
