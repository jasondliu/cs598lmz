import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst

#结果：['', <__main__.A object at 0x00000000029D9E80>, <weakref at 0x00000000029D9F28; to 'A' at 0x00000000029D9E80>]
#说明：当a被删除后，a.c引用计数减一，但是a.c仍然存在，因为keepalive引用了a.c，所以a.c不会被回收，
#所以a.c的引用计数不为0，所以lst[1]不会被回收，所以lst
