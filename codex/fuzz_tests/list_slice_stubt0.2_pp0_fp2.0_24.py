import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用
# 弱引用可以让对象被垃圾回收机制回收，而不是等待变量被删除
# 弱引用不会增加对象的引用计数，因此不会延长对象的生命周期
# 弱引用的引用对象可能会被垃圾回收机制回收，因此弱引用可能会返回None
# 弱引用的引
