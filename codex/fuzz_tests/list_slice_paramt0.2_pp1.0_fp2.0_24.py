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

#结果：['<__main__.A object at 0x0000000003F9C908>']
#因为a.c=a，所以a的弱引用计数为2，所以不会被回收

#练习2
#改写练习1，使得a的弱引用计数为1
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

#结果：[]
#因为a.c=a，所以a的弱引用计
