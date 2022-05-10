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

# 为了解决这个问题，Python 引入了弱引用（weak reference）。弱引用不会增加对象的引用计数，因此不会阻止对象被垃圾回收。
# 弱引用可以使用 weakref 模块中的弱引用类（WeakReference）创建。
# 弱引用对象的回调函数（callback）会在对象被垃圾回收时调用，回
