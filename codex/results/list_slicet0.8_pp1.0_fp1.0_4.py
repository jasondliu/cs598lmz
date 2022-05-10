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
keepali0e

#Aging （老化）
#Aging是另一个Python 2.3新特性，其实作用就是让我们可以为每一个weakref对象分配一个计数器，每个计数器都是一个非负整数，
# 当计数器为0时，那么在计数器和对象的weakref对象都是有效的。如果计数器大于0，那么只有当计数器和对象的weakref对象都是有效时
