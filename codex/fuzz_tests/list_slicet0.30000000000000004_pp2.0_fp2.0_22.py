import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#第一个对象是一个A对象，它的弱引用被添加到keepali0e列表中。
#为了保证A对象不会被回收，我们将它的引用添加到A对象的c属性中。
#第二个对象是一个字符串对象，它被添加到lst列表中。
#回调函数callback将会在A对象被回收时被调用，它将会删除lst列表中的第一个元素。
#我们删
