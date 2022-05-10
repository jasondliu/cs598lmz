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

#结果：
#['', <weakref at 0x00000000025F5A48; to 'A' at 0x00000000025F5B88>]

#结论：
#当一个对象的引用计数为0时，它就会被回收，但是如果它有一个循环引用，那么它就不会被回收。
#如果一个对象有一个弱引用，那么它就会被回收，即使它有一个循环引用。

