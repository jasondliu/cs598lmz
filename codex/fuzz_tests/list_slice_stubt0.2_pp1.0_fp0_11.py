import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(a,callback)
print(lst)
del keepalive
print(lst)

#[<weakref at 0x0000020A9D8E8A48; to 'A' at 0x0000020A9D8E89E8>]
#[None]

#第一个print输出的是一个弱引用对象，第二个print输出的是None，说明弱引用对象已经被回收了。
# 弱引用对象可以被回收，因为它不会增加对象的引用计数，所以当对象的引用计数
