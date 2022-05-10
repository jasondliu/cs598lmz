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
print(lst)
print(keepalive)

#结果：
#['', <weakref at 0x000002A9A7D1A6C8; to 'A' at 0x000002A9A7D1A6D0>]
#[<__main__.A object at 0x000002A9A7D1A6D0>]

#第二个问题：
#结果：
#['', <weakref at 0x000002A9A7D1A6C8; to 'A' at 0x000002A9A7D1A6D0>]
#[<__main__.A object at 0x000002A9A7D1A6D0>]

#第三个问题：
#结果：
#['', <weakref at
