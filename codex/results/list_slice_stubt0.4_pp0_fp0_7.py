import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepali0e.append(a)
keepali0e.append(a.a)
keepali0e.append(a.b)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
del a
del lst
del callback
gc.collect()
print(keepali0e)

# 引用计数
# 引用计数的优点是实现简单，判断一个对象是否存活很快，因为只需要查询一个计数器。
# 引用计数的缺点是维护引用计数消耗资源，而且
