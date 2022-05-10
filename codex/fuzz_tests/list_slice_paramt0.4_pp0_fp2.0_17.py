import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print lst[0]

#练习：使用weakref.ref创建一个弱引用，当引用的对象被删除时，打印出一条消息
import weakref
class A(object):pass
def callback(x):print 'object is deleted'
a=A()
w=weakref.ref(a,callback)
del a
print w()
