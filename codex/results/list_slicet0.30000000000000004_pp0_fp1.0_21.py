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

# 引用计数
# 引用计数器是一个很简单的概念，但是它的实现却是一个很复杂的问题。
# 在Python中，每个对象都有一个引用计数器，当对象被创建时，它的引用计数器被初始化为1，当这个对象不再被使用时，
# 它的引用计数器会递减，当它的引用计数器变为0时，这个对
