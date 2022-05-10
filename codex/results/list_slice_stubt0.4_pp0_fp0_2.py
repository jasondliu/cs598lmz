import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(A(),callback)
print lst
print keepalive
del lst
print keepalive
print keepalive[0].c
print keepalive[0].c.c

#打印结果
#[<weakref at 0x7f6fe8a6e7a0; to 'A' at 0x7f6fe8a6e5d0>]
#[<__main__.A object at 0x7f6fe8a6e590>]
#[<__main__.A object at 0x7f6fe8a6e590>]
#<__main__.A object at 0x7f6fe8a6e590>
#<__main__.A object at 0x7f6fe8a6e590>

#结论：
#1.keepalive不会被回收
#2.keepalive的属性不会
