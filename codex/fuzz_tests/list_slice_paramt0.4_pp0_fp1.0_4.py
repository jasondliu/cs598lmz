import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for x in lst:print x
print keepali0e[0]()
print lst

#['']
#None
#[]

#结果可以看出，当对象的引用计数为0时，触发回调函数，删除lst中的值，但是keepalive中的值依然存在，所以返回None
#如果把keepalive中的值删除，那么keepalive中的值也会被删除，但是lst中的值依然存在，所以返回的是lst中的值

#可以看出
