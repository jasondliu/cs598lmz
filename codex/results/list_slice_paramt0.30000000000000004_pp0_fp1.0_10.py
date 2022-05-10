import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

# 弱引用可以用来缓存数据，并且可以防止缓存的数据无限增长
# 弱引用是一种类似于软引用的东西，它的引用计数永远为0，因此当对象被回收时，它也会被回收
# 弱引用可以用来缓存数据，并且可以防止缓存的数据无限增长
# 弱引
