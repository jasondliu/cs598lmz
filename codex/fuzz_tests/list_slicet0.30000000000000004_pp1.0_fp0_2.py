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

# 引用计数
# 引用计数是一种简单的内存管理机制，它的基本思想是：
# 对象在创建时，其引用计数为1，当对象被别的对象引用时，其引用计数加1，当对象不再被引用时，其引用计数减1，当对象的引用计数为0时，该对象被回收。
# 引用计数的缺
