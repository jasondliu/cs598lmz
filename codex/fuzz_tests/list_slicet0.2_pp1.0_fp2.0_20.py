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

#这个例子中，a.c=a，a引用自身，导致a不能被回收，因为a的弱引用不会被回收，所以a不会被回收。
#这个例子中，a.c=a，a引用自身，导致a不能被回收，因为a的弱引用不会被回收，所以a不会被回收。
#这个例子中，a.c=a，a引用自身，导致a不能被
