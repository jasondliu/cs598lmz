import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
del keepali0e
print(lst)

#weakref.ref(obj,callback) 创建一个弱引用，callback为对象被回收时调用的函数，如果没有指定，则没有回调函数
#weakref.proxy(obj) 返回一个对象的代理，当对象被回收时，代理会自动抛出异常
#weakref.getweakrefcount(obj) 返回对象obj的弱引用计数
#weakref.getweakrefs(obj) 返回对象obj的所有弱引
