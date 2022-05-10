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
# 弱引用是一种特殊的引用，它的引用对象不会增加对象的引用计数，因此当对象的引用计数为0时，对象会被回收。
# 弱引用的作用是避免循环引用，比如：
# 弱引用的创建
# 弱引用的创建使用weakref.ref()方法，它接受一个参数，即要
