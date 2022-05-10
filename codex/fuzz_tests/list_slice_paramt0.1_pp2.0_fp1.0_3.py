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

#这个例子中，a.c=a，这个循环引用会导致a不会被回收，因此callback不会被调用，lst中的元素不会被删除。
#如果将a.c=a这行注释掉，则a会被回收，callback会被调用，lst中的元素会被删除。

#weakref.proxy
#weakref.proxy(object[,callback])
#返回一个代理对象，它引用object，并且在object被回收时，
