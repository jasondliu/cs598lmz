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
#因为a.c=a，所以a不会被回收，所以lst中的元素不会被回收

#练习2
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
#因为a.c=a，所以a不会被回收，所以lst中的元素不会被回收

#练习3
import weakref
class A(
