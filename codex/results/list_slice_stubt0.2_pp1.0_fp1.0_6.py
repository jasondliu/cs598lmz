import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(a,callback)
print(lst)

# 使用weakref.ref()创建弱引用，可以接受一个可选的回调函数，当引用的对象被销毁时，回调函数会被调用。
# 弱引用不会增加对象的引用计数，因此不会阻止对象被垃圾回收机制回收。
# 弱引用的一个常见用途是缓存对象，当对象被
