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
print lst

#结果：
#['', <weakref at 0x0000000003A3C9C8; to 'A' at 0x0000000003A3C948>]
#这个结果说明，当a被删除后，a的弱引用被添加到lst中，但是a的弱引用指向的对象被删除了，所以a的弱引用指向的对象是None

#结论：
#1.弱引用的回调函数会在对象被回收
