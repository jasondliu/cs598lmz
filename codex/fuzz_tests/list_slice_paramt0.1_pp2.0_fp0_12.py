import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：['<__main__.A object at 0x0000000003F8C908>']
#结论：当一个对象的弱引用被删除时，它的回调函数会被调用，但是如果这个对象还有强引用，那么它的回调函数不会被调用。

#练习2：
import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e

#结果：callback
#结
