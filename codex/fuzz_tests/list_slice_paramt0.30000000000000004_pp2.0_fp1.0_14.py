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

#['']

#这个例子中，a的引用计数为1，a.c的引用计数为2，因此a不会被回收，而a.c的弱引用计数为1，因此a.c会被回收，这时a.c的引用计数为1，因此a.c会被回收，这时a.c的引用计数为1，因此a.c会被回收，这时a.c的引用计数为1，因此a.c会被回
