import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a.c,callback)
del a
print wr()
print lst
print keepalive

#输出：
#<__main__.A object at 0x00000000023F4B70>
#[]
#[<__main__.A object at 0x00000000023F4B70>]
#结论：
#弱引用的对象是一个循环引用，弱引用本身也是一个循环引用，因此弱引用不会被回收
#但是当弱引用的对象被回收时，弱引用本身会被回收，回调函数会被
