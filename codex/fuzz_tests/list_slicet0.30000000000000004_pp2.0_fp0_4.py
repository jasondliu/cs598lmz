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
print(keepali0e)

#这个例子中，a对象的引用计数为1，a.c对象的引用计数为2，因为a.c对象指向a对象，所以a对象的引用计数不会为0，a对象不会被回收，因此a.c对象也不会被回收，所以lst[0]对象的引用计数为2，不会被回收。
#这个例子中，a对象的引用计数为1，a.c对
