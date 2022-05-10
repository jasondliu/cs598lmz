import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst[0]

#此处会报错，因为lst[0]已经被删除了
#print lst[0]

#*******************************************************************************************************************************************

#weakref.proxy(object)
#返回一个代理对象，这个代理对象的生命周期取决于object的生命周期
#如果object被删除了，那么代理对象将会抛出ReferenceError异常

import weakref
class A(object):pass
a=A()
p=weakref.proxy(a)
print p
print p.__class__
del a
print p

#*******************************************************************************************************************************************

#weakref.getweakrefcount(object)
#返
