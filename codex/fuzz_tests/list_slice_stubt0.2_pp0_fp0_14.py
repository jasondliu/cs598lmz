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

#[str(), <weakref at 0x0000023B8E0C7F18; to 'A' at 0x0000023B8E0C7E48>]
#[<__main__.A object at 0x0000023B8E0C7E48>]

#第一个str()是因为lst[0]被删除了，所以lst[0]就是str()
#第二个是因为a被删除了，所以a就是str()
#第三个是因为a.c被删除了，所以a.c就是str()
#第四个是因为keepalive被删
