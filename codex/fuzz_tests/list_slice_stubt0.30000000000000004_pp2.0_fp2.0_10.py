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
del lst
print(keepalive)

#[<weakref at 0x000002A5D9C9F948; to 'A' at 0x000002A5D9C9F898>]
#[<__main__.A object at 0x000002A5D9C9F898>]

#如果不加keepalive，则第二个输出为[]
#因为a被删除，所以a.c也被删除，所以a也被删除，所以a.c也被删除，所以a也被删除，所以a.c也被删除
