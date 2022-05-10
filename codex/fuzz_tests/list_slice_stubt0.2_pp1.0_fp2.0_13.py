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
print(lst)
del keepalive
print(lst)

#结果：
#[str(), <__main__.A object at 0x000002A9D5E5F9B0>, <weakref at 0x000002A9D5E5F9E8; to 'A' at 0x000002A9D5E5F9B0>]
#[str(), <weakref at 0x000002A9D5E5F9E8; dead>]
#结论：
#当a被删除时，a.c引用a，a.c被keepalive引用，所以a不会被回收，lst[1]也不会被回收，
#
