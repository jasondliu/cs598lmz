import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['abc']
#因为a.c=a，所以a的引用计数为2，所以a不会被回收，所以lst[0]不会被回收

#例子2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：[]
#因为a.c=a，所以a的引用计数为2，所以a不会被回收，所以
