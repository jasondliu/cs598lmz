import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive[:]
gc.collect()
print lst

#[str(), <weakref at 0x0000000002A6B988; to 'A' at 0x0000000002A6B908>]

#可以看到，在回调函数中，对象a的引用计数为0，但是依然存在，这是因为在回调函数中，对象a的弱引用计数还是1，所以对象a依然存在。

#这个例子中，回调函数中，对象a的弱引用计
