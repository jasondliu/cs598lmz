import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(len(lst))
print()

#weakref.ref(obj,callback)

#可以用一个回调函数让对象在被回收时做一些事情

#weakref.proxy(obj,callback)

#返回一个对象的代理对象，当对象被回收时，代理对象会抛出ReferenceError异常

#weakref.getweakrefcount(obj)

#返回弱引用对象的数量

#weakref.getweakrefs(obj)

#返回弱引用对象的列表

#weakref
