import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print(lst)

#清理垃圾时，会调用回调函数，删除列表中的第一个元素

#weakref.proxy(object,callback)
#返回一个弱引用的代理对象，当被代理的对象被清理时，会调用回调函数

#weakref.getweakrefcount(object)
#返回对象的弱引用数量

#weakref.getweakrefs(object)
#返回对象的弱引用列表

#weakref.finalize(object,callback)
#创建一个对
