import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
print(lst)
del a
print(lst)

# 弱引用
# 弱引用是一种特殊的引用，它的引用计数不会增加对象的引用计数。
# 弱引用的目的是允许对象被垃圾回收时被删除，而不是等待引用计数变为0。
# 弱引用可以使用weakref模块来创建。
# 弱引用可以使用weakref.ref()来创建。
# 弱引用可以使用weakref.proxy
