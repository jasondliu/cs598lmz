import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
#可以看出，弱引用是同时引用两个对象的，其中一个对象被删除后，其他引用的弱引用也会被删除
#弱引用的删除不会触发垃圾回收，但是会触发现有的回收机制
print(lst)
