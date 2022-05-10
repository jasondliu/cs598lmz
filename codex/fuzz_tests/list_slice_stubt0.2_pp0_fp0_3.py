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
print lst
print keepalive

#[str(), <weakref at 0x7f9f9b7e0d08; to 'A' at 0x7f9f9b7e0d50>]
#[<__main__.A object at 0x7f9f9b7e0d50>]

#这里的a.c=a，是为了让a对象的引用计数为2，这样在del a的时候，a对象的引用计数才不会为0，
#这样a对象才不会被回收，这样就可以看到弱引用的回调函数callback的
