import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(a.c)
keepalive.append(lst)
keepalive.append(callback)
w=weakref.ref(a,callback)
del a
del keepalive
print(lst)

#这个例子中，对象a指向自身，导致w引用a，因此a不会被回收。
#当w被删除时，回调函数callback被调用，删除lst[0]，导致lst被回收，因此a被回收。
#这个例子中，a的弱引用被删除，因此a
