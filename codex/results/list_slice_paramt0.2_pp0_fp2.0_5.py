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

#这个例子中，a.c=a，这样a和a.c引用了同一个对象，所以a.c的引用计数为2，
# 因此，a.c不会被回收，a.c引用的对象也不会被回收，所以lst中的元素不会被回收，
# 因此lst中的元素不会被删除，所以lst中的元素不会被删除，所以lst中的元素不会被删除，

