import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

# 弱引用
# 弱引用是一种特殊的引用，它的引用对象不会增加对象的引用计数，因此当对象的引用计数为0时，对象会被垃圾回收机制回收。
# 弱引用的作用是在不影响对象生命周期的情况下，提供一种对对象的句柄。
# 弱引用的实现是通过内
