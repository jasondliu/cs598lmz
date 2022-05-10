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

#output:['<__main__.A object at 0x7f8b8c8c3f90>']

#结论：当一个对象的弱引用被回调时，它的引用计数不会被减少，因此它不会被回收。
#只有当它的引用计数为0时，它才会被回收。
