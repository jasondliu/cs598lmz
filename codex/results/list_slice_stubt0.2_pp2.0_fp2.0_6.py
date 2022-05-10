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
del keepalive[0]
print(lst)

#结果：['', <weakref at 0x000002A8B0C8A9D8; to 'A' at 0x000002A8B0C8A9C0>]
#结论：当回调函数被调用时，弱引用对象的引用计数为0，但是它的__del__方法并不会被调用，因为它的引用计数为0，所以它不会被放入垃圾回收队列中。

#结论：当
