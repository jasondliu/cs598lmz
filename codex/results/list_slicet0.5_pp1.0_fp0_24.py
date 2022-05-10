import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#可以看到，当del a的时候，虽然a的引用计数变为0，但是由于a.c=a，因此a的弱引用计数仍然为1，所以a并没有被垃圾回收。
#当lst[0]被删除的时候，a的弱引用计数变为0，因此a被垃圾回收。

#弱引用的作用就是在对象被垃圾回收的时候，调用自定义的函数。
#弱引用的
