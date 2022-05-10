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

#结果：['<__main__.A object at 0x000002A0A8E8C908>']
#结论：当对象a被删除时，a.c引用计数减1，但是a.c还是引用了a，所以a的引用计数不为0，所以a不会被回收，所以lst中的元素不会被删除

#练习2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.
