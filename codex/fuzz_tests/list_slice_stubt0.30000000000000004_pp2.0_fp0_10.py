import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.a=weakref.ref(a,callback)
del a
print(lst)

#结果为：['\x00']
#结论：弱引用的回调函数会在引用对象被回收的时候调用，但是如果引用对象的引用计数为0，但是还有引用对象的引用，那么引用对象不会被回收，回调函数也不会被调用
#这里的引用对象是a，a.a是对a的弱引用
