import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
del a
del keepalive[:]
print(len(lst))#0

#weakref.proxy(obj[,callback])
#返回一个代理对象，它会持有obj的弱引用，当obj被垃圾回收的时候，代理对象就会被自动销毁。
#当代理对象被访问的时候，它会检查obj是否还存在，如果存在，它会转发调用给obj，否则抛出ReferenceError异常。
#如果obj
