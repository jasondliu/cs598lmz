import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.x=weakref.ref(lst,callback)
lst=None
print len(keepalive)
del keepalive[0]
print len(keepalive)

#结果：
#1
#0

#这个例子展示了，当弱引用的对象被回收时，回调函数会被调用。
#回调函数的参数是弱引用对象。
#回调函数可以访问弱引用对象，但是不能保留对它的引用。
#回调函数可以修改弱引用对象的
