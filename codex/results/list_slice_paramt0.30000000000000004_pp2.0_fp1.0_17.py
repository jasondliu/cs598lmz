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

#weakref.ref(object[,callback])
#创建一个弱引用，当被引用的对象被销毁时，会调用回调函数
#callback可以是一个函数或者一个可调用对象，如果没有指定回调函数，则弱引用对象不会被销毁
#返回一个弱引用对象，该对象支持和普通引用一样的操作，但是不会增加被引用对
