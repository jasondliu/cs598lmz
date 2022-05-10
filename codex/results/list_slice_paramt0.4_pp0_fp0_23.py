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

#答案：['',]
#答案解析：
#先来看下weakref.ref()的定义，它的第一个参数是要弱引用的对象，第二个参数是回调函数，当被引用的对象被删除时，会调用该回调函数。
#在这个例子中，a被引用了两次，一次是弱引用，一次是普通引用，因此a不会被删除。
#首先
