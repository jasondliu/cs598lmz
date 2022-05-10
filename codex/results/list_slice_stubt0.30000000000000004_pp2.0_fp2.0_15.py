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
print lst

#output:
#['\x00']

#结论：
#当一个对象的弱引用计数为0时，即使它还有强引用，也会被回收。
#当弱引用计数为0时，它的回调函数也会被调用。
#当一个对象的弱引用计数为0时，它的回调函数会被调用，但是它的强引用不会被回收。
#当一个对
